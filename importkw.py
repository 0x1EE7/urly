#!/usr/bin/env python
import sys
import logging
import sqlite3
from optparse import OptionParser


URL = 'http://techcrunch.com/2012/12/28/pinterest-lawsuit/'


def main():
    import_keywords_to_db()


def import_keywords_to_db():
    usage = '%prog -f <file> -d <database>'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', help='keyword file to import',
                      metavar='FILE', dest='file')
    parser.add_option('-d', '--database', help='sqlite3 database',
                      metavar='FILE', dest='db')
    (options, args) = parser.parse_args()

    if (not options.file) or (not options.db):
        parser.print_usage()
        logging.error('Got no or invalid arguments, exiting.')
        sys.exit(1)

    keywords = read_keywords(options.file)
    bulk_insert(keywords, options.db)
    print len(keywords)


def bulk_insert(keyword_set, db_file):
    '''
    Inserts the words in keyword set into 'words' table in DB.
    '''
    l = [(k.decode('UTF-8'), '', None) for k in keyword_set]
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.executemany('INSERT INTO urly_shorturl VALUES (?,?,?)', l)
        conn.commit()
        conn.close()
    except:
        raise
    print 'Success'


def read_keywords(keyword_file):
    '''
    Reads file and adds keywords to hashset. Returns populated set object.
    '''
    keys = set()
    delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    file = open(keyword_file)
    for line in file:
        keys.add(line.translate(None, delchars).lower())
    return keys

if __name__ == '__main__':
    main()
