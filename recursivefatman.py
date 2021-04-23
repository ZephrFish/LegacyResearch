#!/usr/bin/python
# Recursive Fatman
# Python 2
import dns.query
import dns.zone
import dns.resolver
from multiprocessing import Pool
def execute_tests():
  with open('url.txt', 'r') as f:
    for line in f: 
      findns(line)

#def findns(line):
#  with open('url.txt', 'r') as f:
 #   for line in f:
  
  
       
 # ztit(ns, line)
 # recurtest(ns)

def ztit(line):
  line = line.replace("www.", "")
  print "Trying ", line
  try:
    ns = dns.resolver.query(line.strip(), 'NS') 
    for ser in ns.rrset:
      server = str(ser)[:-1] 
      if server is None or server == "":
        continue

      print "Trying NS ", server
      
      try:
        z = dns.zone.from_xfr(dns.query.xfr(str(server), line.strip(), lifetime=5))
      except:
        z = None
      if z is not None:   
        fn = line.strip() + '-output.txt'
        f2w = open(fn, "w")
        for name, node in z.nodes.items():
          rdataset = node.rdatasets
          for rdata in rdataset:
            f2w.write(str(name) + " " + str(rdata) +"\n")
        f2w.close()
        print "Transfer Worked, Writing to file."+ line.strip() +"-output.txt"
        # reporter(z, line.strip(), server)       
       # with open(fn, 'w') as d:
        #  names = z.nodes.keys()
        #  names.sort()
        #  i = 'Vulnerable Name Server! ' + server + '\n'
        #  d.write(i)
        #  for x in names:
        #    s = z[x].to_text(x) + '\n'
        #    d.write(s)
      else:
        continue
  except: 
    print "No Answer "
   # continue
def recurtest(ns):
  for i in ns:
    query = dns.resolver.Resolver()
    query.nameservers[i]
    answer = query.query('google.com', 'A')
    for host in answer:
      print host
  
def reporter(z, server, ns):
  fn = server.strip() + '-output.txt'
  with open(fn, 'w') as d:
    names = z.nodes.keys()
    names.sort()
    i = 'Vulnerable Name Server!' + ns + '\n'
    d.write(i)
    for x in names:
      s = z[x].to_text(x) + '\n'
      d.write(s)
  print i

def main():
  dom = Pool(processes=21) # Change this line to alter the amount of threads used for checking
  mains = open("miss.txt", "r").readlines() # Change miss.txt to file 
  dom.map(ztit, mains)
  #findns()

main()
