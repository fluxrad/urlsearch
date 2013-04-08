#!/usr/bin/env python
""" A class to check on a URL and see if a specified string exists. """
import urllib2
import boto
import ConfigParser

class URLSearch:
    def __init__(self):
        """ Create a URLSearch object. Open config and read settings """
        config = ConfigParser.ConfigParser()
        config.readfp(open('urlsearch.cfg'))
        self.search_url = config.get('main', 'search_url')
        self.search_string = config.get('main', 'search_string')
        self.notify_string = config.get('main', 'notify_string')

        try:
            self.sns_topic = config.get('main', 'sns_topic')
            self.sns_region = config.get('main', 'sns_region')
        except (NameError, ConfigParser.NoOptionError):
            print "No SNS information specified. Not using SNS."
            self.sns_topic = None
            self.sns_region = None

    def search_for_string(self):
        """ Search the URL for the existence of search_string. Return true or
        false depending whether or not the string was found. """
        response = urllib2.urlopen(self.search_url)
        html = response.read()
        if html.find(self.search_string):
            print "String found: {0}".format(self.search_string)
            return True
        else:
            print "String not found: {0}".format(self.search_string)
            return False

    def notify(self):
        print "{0}".format(self.notify_string)
        if self.sns_topic and self.sns_region:
            print "Notifying SNS topic: {0}".format(self.sns_topic)
            boto.connect_sns()
            sns = boto.sns.connect_to_region(self.sns_region)
            sns.publish(self.sns_topic, self.notify_string)

if __name__ == "__main__":
    s = URLSearch()
    if s.search_for_string() == False:
        # Send a notification if the search string isn't found (my own use
        # case). If you want to notify when a string is found, just change the
        # above to == True
        s.notify()
