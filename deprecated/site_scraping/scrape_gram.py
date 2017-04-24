from __future__ import print_function
from lxml import html
import requests
import time
import sys


with open('bacteria/scraped_names.txt', 'r') as handle:
    with open('bacteria/scraped_gram.txt', 'w') as outfile:
        count = 0
        last_progress = 0
        total = 1
        for line in handle:
            if line.startswith('##'):
                count = 0
                last_progress = 0
                total = float(line.strip().split()[1])
                print('\n')
                print(line)
                print('----------------------------------------------------------------------------------------------------')
                time.sleep(5)
                continue

            if '..' in line:
                line = line.replace('protocols/Bacterialspecies/../../','')

            bact = line.strip().split('\t')
            bact_page = requests.get(bact[0])
            bact_tree = html.fromstring(bact_page.content)
            gram = bact_tree.xpath('.//child::*[contains(text(), "am stain")]')

            if gram:
                outfile.write(bact[1] + '\t' + gram[0].text_content().rsplit(' ', 1)[-1].strip('.'))
                outfile.write('\n')
                count += 1
            else:
                outfile.write(bact[1] + '\t' + 'unknown')
                outfile.write('\n')
                count += 1

            current_progress = int(count/total*100)
            print((current_progress-last_progress)*'#', end='')
            sys.stdout.flush()
            time.sleep(0.1)
            last_progress = current_progress
