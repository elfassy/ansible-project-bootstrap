#!/usr/bin/env python

import os
import time

from subprocess import Popen, PIPE, STDOUT

certs = {{letsencrypt_certs}}

script = "{{ acme_tiny_software_directory }}/acme_tiny.py"

for cert in certs:
    if os.access(cert['certpath'], os.F_OK):
        stat = os.stat(cert['certpath'])
        print "Certificate file " + cert['certpath'] + " already exists"

        if time.time() - stat.st_mtime < {{ letsencrypt_min_renewal_age }} * 86400:
            print "  The certificate is younger than {{ letsencrypt_min_renewal_age }} days. Not creating a new certificate.\n"
            continue

    host = ",".join(cert['host']) if type(cert['host']) is list else cert['host']

    print "Generating certificate for " + host
    args = [
        "python", script,
        "--account-key",
        "{{ letsencrypt_account_key }}",
        "--csr",
        "{{ acme_tiny_data_directory }}/csrs/" + cert['name'] + ".csr",
        "--acme-dir",
        "{{ acme_tiny_challenges_directory }}"
    ]

    cmd = "/usr/bin/env " + " ".join(args)
    print cmd
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
    output = p.stdout.read()
    p.stdin.close()
    if p.wait() != 0:
        print "error while generating certificate for " + host
        print p.stderr.read()
    else:
        print "Writing file " + cert['certpath']
        f = open(cert['certpath'], 'w')
        f.write(output)
        f.close()

    print "Writing file " + "{{letsencrypt_intermediate_cert_path}}"
    with open(cert['chainedcertpath'], 'wb') as outFile:
        with open(cert['certpath'], 'rb') as com, open('{{letsencrypt_intermediate_cert_path}}', 'rb') as fort13:
            outFile.write(com.read())
            outFile.write(fort13.read())
            outFile.close()
