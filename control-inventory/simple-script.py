#!/usr/bin/python
import sys

import json

atl = {
    'hosts': [ 'host1', 'host2']
}
rdu = {
    'hosts': [ 'host2', 'host3']
}
se = {
    "children": [ 'atlanta', 'raleigh' ],
    "vars": {
        "nameserver": "dns.southeast.example.com",
        "halon_system_timeout": 30,
        "self_destruct_countdown": 60,    
        "escape_pods": 2
    }
}

usa = {
    "children": [ 'southeast' ]
}

inv = { 'atlanta': atl, 'raleigh': rdu, 'southeast': se, 'usa': usa, '_meta' : { 'hostvars': {} } }

if len(sys.argv) > 1 and sys.argv[1] == '--list':
    print json.dumps(inv)
