from lxml import html
import requests
import sys


base_href = 'http://www.thelabrat.com/protocols/Bacterialspecies/'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for l in alphabet:
    links = []
    name_page = requests.get('http://www.thelabrat.com/protocols/Bacterialspecies/byname%s.shtml' % l)
    name_tree = html.fromstring(name_page.content)
    bacts = name_tree.xpath('/html/body/table[1]/tr[3]/td/table[1]/tr/td[2]/table[1]/tr/td/table[3]/descendant::a')
    print '##%s ' % l + str(len(bacts))
    for b in bacts:
        name = b.text
        if not name:
            children = b.getchildren()
            if len(children):
                name = children[len(children) - 1].text
        name = name.replace('\t', ' ')
        links.append(base_href+b.attrib['href'] + '\t' + name)
    for link in links:
        print link
