#!/usr/bin/python

import sys, os, time
import subprocess
from art import tprint       
############## GLOBAL VARIABLES ###################
welcome = "toilet -F border:gay Welcome to MTB-VCF"
subprocess.check_call(welcome, shell=True)
def downloading_dependencies():
		print("""##############################Downloading Dependencies##############################""")
		tprint("Downloading   Dependencies")
		sources = "sudo cp sources.list /etc/apt/"
		subprocess.check_call(sources, shell=True)
		bwa = "sudo apt-get install bwa"
		subprocess.check_call(bwa, shell=True)
		tabix = "sudo apt-get install tabix"
		subprocess.check_call(tabix, shell=True)
		samtools = "sudo apt-get install samtools"
		subprocess.check_call(samtools, shell=True)
		picard = "sudo apt-get install picard-tools"
		subprocess.check_call(picard, shell=True)
		parallel = "sudo apt-get install parallel"
		subprocess.check_call(parallel, shell=True)
		bcf = "sudo apt-get install bcftools"
		subprocess.check_call(bcf, shell=True)
downloading_dependencies()
tprint("Ready   to   run   your   script")

