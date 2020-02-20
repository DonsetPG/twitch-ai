import  progressbar
import  sys 
import  os
import  pandas  as pd
from    absl    import flags
from    absl    import app

from typing import List, Set, Dict, Tuple, Optional

"""

python3 log_to_csv.py --log_path 'sardo_live_nocturne.log' \
                      --csv_path 'sardo_live_nocturne.csv'

"""

flags.DEFINE_string('log_path',
                    None,
                    'Input path of the log file to convert')
flags.DEFINE_string('csv_path',
                    None,
                    'Output path of the csv file to save')



sender_mapping = {
                    "!": "admin",
                    "$": "bits",
                    "~": "broadcaster",
                    "*": "global_mod",
                    "@": "moderator",
                    "+": "premium",
                    "&": "staff",
                    "%": "subscriber"
                 }

FLAGS = flags.FLAGS

def _splitter(line: str) -> Tuple:
    """Takes a line from the .log file and retrieve useful informations
    Args:
        line: The line to process
    Returns:
        type_sender: The type of sender from sender_mapping
        time_: The time the message was sent 
        sender_: Who sent the message
        new_line: The content of the message

    """
    #Splitting the time
    end_time: int = line.find(']')
    time_: str = line[1:end_time]
    new_line: str = line[end_time+3:]
    # Retrieving the sender type if it exists
    type_sender: str = 'none'
    if new_line[0] in sender_mapping: 
        type_sender = sender_mapping[new_line[0]]
        new_line = new_line[1:]
    # Retrieving the sender's name
    end_sender: int = new_line.find('>')
    sender_: str = new_line[:end_sender]
    # Content of the message
    new_line = new_line[end_sender+2:-1]
    new_line = new_line.replace(',',';')

    return type_sender, time_, sender_, new_line

def _read_log(log_path: str) -> Dict:
    """Reads a .log and returns a dict with the wanted informations
    Args:
        log_path: The path of the .log file
    Returns:
        log_to_dict: A dict with the valuable informations

    """
    log_to_dict: Dict  = {
        'Time':[],
        'Sender':[],
        'Sender_type':[],
        'Content':[]
    }

    f = open(log_path,'r')
    f_ = f.readlines() 
    for line in progressbar.progressbar(f_):
        type_sender, time_, sender_, text = _splitter(line)
        log_to_dict['Time'].append(time_)
        log_to_dict['Sender'].append(sender_)
        log_to_dict['Sender_type'].append(type_sender)
        log_to_dict['Content'].append(text)
    f.close() 

    return log_to_dict 

def main(argv):

    if os.path.splitext(FLAGS.csv_path)[1] == '.csv':
        log_to_dict = _read_log(FLAGS.log_path)
        df_log = pd.DataFrame(log_to_dict)
        df_log.to_csv(FLAGS.csv_path)
    else:
        print('{} is not a csv file format...'.format(FLAGS.csv_path))
        print('Transcript aborted')


if __name__ == "__main__":
    flags.mark_flag_as_required("log_path")
    flags.mark_flag_as_required("csv_path")
    app.run(main)

