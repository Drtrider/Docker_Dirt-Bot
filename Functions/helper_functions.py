from datetime import datetime
import logging
import os


def setup_logging():
    '''
    Used to initilize logging configs to spit out in the right location
    DEPENDANCY CAUTION:  Must have  'import logging'   imported
    DEPENDANCY CAUTION:  Must have  'from datetime import datetime'    imported

    Example of writing to the log
    logging.critical('This is a log message..')
    logging.error('This is a log message..')
    logging.warning('This is a log message..')
    logging.info('This is a log message..')
    logging.debug('This is a log message..')
    logging.notset('This is a log message..')
    '''

    # Setup string vars to check for log file
    connected_volume_file_path = "/drt-bot-data"

    # Check for a log file, if there isn't one, try to create one.
    create_log_file_retry_count = 0
    while create_log_file_retry_count < 1:
        is_log_directory_found = os.path.isdir(
            connected_volume_file_path + "/Logs")

        if is_log_directory_found == True:
            print("Log folder found in connected volume! Continuing log setup...")
            break

        else:
            print(
                "No log folder found at path: {is_log_directory_found} \nAttempting to create one...")
            os.mkdir("Functions/Logs")
            create_log_file_retry_count += 1

    if is_log_directory_found != True:
        raise ValueError(
            "WARINING: Unable to create log folder at {is_log_directory_found}!!!")
    # End While Loop

    # Build all filepathes needed to store logs in a connected volume.
    logFileName_dateTimeStamp = datetime.now().strftime("%Y_%m_%d")
    full_log_filename_string = connected_volume_file_path + \
        "Logs/" + logFileName_dateTimeStamp + ".log"

    # Set logging config(s)
    logging.root.handlers = []
    logging.basicConfig(
        format='[%(asctime)s] (%(filename)s:%(lineno)s) [%(levelname)s] %(message)s',
        level=logging.NOTSET, filename=full_log_filename_string
    )

    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(logging.NOTSET)

    # set a format which is simpler for console use
    formatter = logging.Formatter(
        '[%(asctime)s] (%(filename)s:%(lineno)s) [%(levelname)s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
