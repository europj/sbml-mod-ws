# -*- encoding: UTF-8 -*-
import ConfigParser
import logging
import os


# Root directory for the BlastWS
filepath = os.path.abspath(__file__)
basepath = os.path.dirname(filepath)
srcpath = os.path.split(basepath)[0]
ROOT_DIR = os.path.split(srcpath)[0]

# Read config file
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join('parts', 'etc', 'pyserver.cfg')))

FILES_DIR = os.path.join(ROOT_DIR, 'parts', 'directories', 'pyserver')

# Web service port
SERVER_CODE_DIR = config.get('WebService', 'servercodedir')
WSDL = os.path.join(ROOT_DIR, SERVER_CODE_DIR, config.get('WebService', 'wsdl'))
WS_PORT = int(config.get('WebService', 'port'))

# Settings for logging
LOG_DIR = os.path.join(FILES_DIR, 'log')
SERVERD_LOG_FILE = os.path.join(LOG_DIR, 'serverdaemon.log')
SERVICE_LOG_FILE = os.path.join(LOG_DIR, 'service.log')
LOG_LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
DEFAULT_LOG_LEVEL = config.get('Logging', 'defaultlevel')
MAX_BYTES = 1048576
BACKUP_COUNT = 5

# Settings for server daemon
SERVERD_PID_FILE = os.path.join(LOG_DIR, 'serverdaemon.pid')

# Creating dir and files as part of buildout
def generate_directories(options, buildout):
    if not os.path.isdir(FILES_DIR):
        os.mkdir(FILES_DIR)
    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)
        os.mknod(SERVERD_LOG_FILE)
