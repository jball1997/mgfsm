from pathlib import Path
import sys
from tqdm import tqdm

if len(sys.argv) < 2 or (sys.argv[1] != '0' and sys.argv[1] != '1'):
  print('usage: python create_symlinks.py (0 | 1)')
  sys.exit()

if sys.argv[1] == '0':
  path = '../CodeInquisitor/PATTERN_ANALYSIS/blackbox_time_series'
else:
  path = '../CodeInquisitor/PATTERN_ANALYSIS/blackbox_time_series_Jan_July_2019_w_timestamps'

with open('BLACKBOX_INPUT/input.txt', 'w') as input_f:
  pathlist = Path(path).glob('*/*')
  for path in tqdm(list(pathlist)):
    path_in_str = str(path) + '/events'
    try:
      with open(path_in_str, 'r') as f:
        content = f.read().split(',')
        # skipping sessions where less than 10 events happen
        if len(content) < 10:
          continue
        # aggregate all consecutive edits into one
        aggregated_content = []
        ON_REPETITIVE_EVENT = False
        for event in content:
          if event in ('22', '19', '20', '8', '9', '47') and not ON_REPETITIVE_EVENT:
            ON_REPETITIVE_EVENT = True
            aggregated_content.append(event)
          elif event in ('22', '19', '20', '8', '9', '47') and ON_REPETITIVE_EVENT:
            pass
          else:
            ON_REPETITIVE_EVENT = False
            aggregated_content.append(event)
        events = ' '.join(aggregated_content)
        input_f.write(events)
        input_f.write('\n')
    except FileNotFoundError:
      pass
