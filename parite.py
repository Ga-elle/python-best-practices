#! /usr/bin/env python3
# coding: utf-8

import argparse
import logging as lg
import re

import analysis.csv as c_an
import analysis.xml as x_an


def parse_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of information about the members of parliament""")
  parser.add_argument("-v", "--verbose", help="""Make the application talk""")
  parser.add_argument("-i", "--info", action='store_true', help="""Information about the file""")
  return parser.parse_args()

def main():
  args = parse_arguments()
  
  #import pdb; pdb.set_trace()
  
  if args.verbose:
    lg.basicConfig(level=lg.DEBUG)
  
  try:
    datafile = args.datafile
    if datafile == None:
      raise Warning('You must indicate a datafile')
    else:
      try:
        #- Find the extension of the file
        e = re.search(r'^.+\.(\D{3})$', args.datafile)
        extension = e.group(1)
        print(extension)
        
        if extension == 'xml':
          x_an.launch_analysis(datafile)
        if extension == 'csv':
          c_an.launch_analysis(datafile, info=args.info)
      except FileNotFoundError as e:
        lg.error("Ow: ( The file was not found. Here is the original message of the exception:", e)
      except:
        lg.error("Destination unknown")
      finally:
        lg.info("####################### Analysis is over ###########################")
              
  except Warning as e:
    lg.warning(e)

if __name__ == "__main__":
  main()