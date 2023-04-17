#!/usr/bin/python

"""
#-------   DESCRIPTION   --------
#------TO RUN THIS PROJECT-------
# python PROJECT -i yourinputfile.vcf
# python PROJECT -i /path/to/yourinputfile.txt -o /path/to/output.vcf 
"""

import sys, os, time
import subprocess
from argparse import ArgumentParser
from art import tprint

############## GLOBAL VARIABLES ###################
GATK="software/GenomeAnalysisTK.jar"
knownSites="ref/MTB_Base_Calibration_List.vcf"
SAMPLE="fq/sample.txt"
FQ="fq/{1}_*fastq"
TUBERCULOSIS ="ref/M._tuberculosis_H37Rv_2015-11-13.fasta"
JDK = "tar -zxvf /software/jdk-8u211-linux-x64.tar.gz"
JAVA="software/jdk1.8.0_211/bin/java"
PARA='parallel -j 4 --colsep "\\t"'

############## DOWNLOADING SOFTWARES ###################
#def downloading_dependencies():
 #       print("""##############################Downloading Dependencies##############################""")
  #      tprint("Downloading Dependencies")
#	sources = "sudo cp sources.list /etc/apt/"
#	subprocess.check_call(sources, shell=True)
#	bwa = "sudo apt-get install bwa"
#	subprocess.check_call(bwa, shell=True)
#	tabix = "sudo apt-get install tabix"
#	subprocess.check_call(tabix, shell=True)
#	samtools = "sudo apt-get install samtools"
#	subprocess.check_call(samtools, shell=True)
#	picard = "sudo apt-get install picard-tools"
#	subprocess.check_call(picard, shell=True)
#	parallel = "sudo apt-get install parallel"
#	subprocess.check_call(parallel, shell=True)
#	bcf = "sudo apt-get install bcftools"
#	subprocess.check_call(bcf, shell=True)

############## RUN COMMANDS ###################
tool_name="toilet -f mono9 -F border:gay MTB-VCF"
subprocess.check_call(tool_name, shell=True)
def commands(SAMPLE,OUTF,ANN,MERGE,FILT):
            cmd0=PARA+""" 'bwa mem -M -R "@RG\\tID:{1}\\tLB:{2}\\tPL:ILLUMINA\\tPM:HiSeq2000\\tSM:{1}" """+TUBERCULOSIS+""" """+FQ+""" > {1}.sam' :::: """+SAMPLE
            cmd1=PARA+""" 'picard-tools SortSam I={1}.sam O={1}_sorted.bam SORT_ORDER=coordinate' :::: """+SAMPLE
            cmd2=PARA+' '+""" 'picard-tools MarkDuplicates INPUT={1}_sorted.bam OUTPUT={1}_sorted_dedup.bam METRICS_FILE={1}_metrics.txt' :::: """+SAMPLE
            cmd3=PARA+' '+""" 'picard-tools BuildBamIndex I={1}_sorted_dedup.bam' :::: """+SAMPLE
            cmd4=PARA+' '+"""'"""+JAVA+' -Xmx8G -jar '+ GATK +' -T RealignerTargetCreator -R '+TUBERCULOSIS+' -rf BadCigar -I {1}_sorted_dedup.bam -o {1}_sorted_dedup_bam_realignment_targets.list --allow_potentially_misencoded_quality_scores'+"""' :::: """+SAMPLE
            cmd5=PARA+' '+"""'"""+JAVA+' -Xmx8G -jar '+ GATK +' -T IndelRealigner -R '+TUBERCULOSIS+' -rf BadCigar --consensusDeterminationModel USE_READS -I {1}_sorted_dedup.bam -targetIntervals {1}_sorted_dedup_bam_realignment_targets.list -o {1}_sorted_dedup_realigned_reads.bam --allow_potentially_misencoded_quality_scores'+"""' :::: """+SAMPLE
            cmd6 =PARA+' '+"""'"""+JAVA+' -Xmx8G -jar '+ GATK +' -T BaseRecalibrator --interval_padding 50  -R '+TUBERCULOSIS+' -rf BadCigar -knownSites ref/MTB_Base_Calibration_List.vcf -I {1}_sorted_dedup_realigned_reads.bam -o {1}_sorted_dedup_realigned_reads.bam_recal_data.table'+"""' :::: """+SAMPLE
            cmd7 =PARA+' '+"""'"""+JAVA+' -Xmx8G -jar '+ GATK +' -T PrintReads -R '+TUBERCULOSIS+' -rf BadCigar -BQSR {1}_sorted_dedup_realigned_reads.bam_recal_data.table -I {1}_sorted_dedup_realigned_reads.bam -o {1}_sorted_dedup_realigned_reads_recal.bam --allow_potentially_misencoded_quality_scores'+"""' :::: """+SAMPLE
            cmd8 =PARA+' '+"""'"""+JAVA+' -Xmx8G -jar '+ GATK +' -T HaplotypeCaller -R '+TUBERCULOSIS+' --interval_padding 50 -I {1}_sorted_dedup_realigned_reads_recal.bam -L ref/effluxgenes.bed -ploidy 1 -o {1}_efflux_ploidy1.vcf'+"""' :::: """+SAMPLE
            subprocess.check_call(cmd0, shell=True)
            subprocess.check_call(cmd1, shell=True)
            subprocess.check_call(cmd2, shell=True)
            subprocess.check_call(cmd3, shell=True)
            subprocess.check_call(cmd4, shell=True)
            subprocess.check_call(cmd5, shell=True)
            subprocess.check_call(cmd6, shell=True)
            subprocess.check_call(cmd7, shell=True)
            subprocess.check_call(cmd8, shell=True)
            if (MERGE):
                    cmd9 = "ls *vcf > vcf.list"
                    subprocess.check_call(cmd9, shell=True)
                    cmd10 =JAVA+' -Xmx8G -jar '+ GATK +' -T CombineVariants -R '+TUBERCULOSIS+' -V vcf.list -genotypeMergeOptions REQUIRE_UNIQUE -o combine_ploidy.vcf'
                    subprocess.check_call(cmd10, shell=True)
            if (ANN):
                    cmd11= "bcftools csq -f ../../../ref/M._tuberculosis_H37Rv_2015-11-13.fasta -g ../../../ref/h37rv.gff combine_ploidy.vcf -Oz -o annotated.vcf.gz"
                    subprocess.check_call(cmd11, shell=True)
            if (FILT):
                    cmd12 = "bcftools query -f'[%CHROM\t%POS\t%REF|%ALT\t%SAMPLE\t%TBCSQ\n]' annotated4001stbatch.vcf.gz"
                    subprocess.check_call(cmd12, shell=True)
            # Removing files
            subprocess.check_output("rm file_to_remove.txt", shell=True)
            subprocess.check_output("rm file_to_remove.html", shell=True)

############## MAIN PROCESS ###################
if __name__ == '__main__':
        tprint("Running VCF Pipeline")
        print("\n\n")
        
        ## Parsing arguments
        parser = ArgumentParser(description="Description of project..")
        parser.add_argument("-i", "--infile", dest="INPUTFile",default=False, required=True, help="Full path of the input sample file.")
        parser.add_argument("-o", "--outdir", dest="OUTPUTDirectory",default="./", required=False, help="Output directory")
        parser.add_argument("-a", "--annotate", dest="ANNOTATEFile",default=False, required=False, help="To annotate variants.")
        parser.add_argument("-m", "--merge", dest="MERGEFile",default=False, required=False, help="To merge multiple vcf into single multi-sample vcf file.")
        parser.add_argument("-f", "--filter", dest="FILTERFile",default=False, required=False, help="To filter the vcf file.")

        ## Assign arguments to global variables
        args = parser.parse_args()
        #GATK = args.GATK_path

	## Inputs / Outputs path & names
        SAMPLE = args.INPUTFile
        OUTF = args.OUTPUTDirectory
        ANN = args.ANNOTATEFile
        MERGE = args.MERGEFile
        FILT = args.FILTERFile
        TMPDIR = os.path.dirname(os.path.abspath(OUTF)) + "/project_tmp/"
        subprocess.check_output("mkdir -p " + TMPDIR, shell=True)

        ## Check if global variables point to existing files:
        INF_check = os.path.exists(SAMPLE)
        OUT_check = os.path.exists(GATK)

        if not(INF_check and OUT_check):
                print(">ERROR : One or several global variable: \n  Input={} > {}\n  Output directory={} > {}\n>Please correct and try again!".format(INF, INF_check, OUT,OUT_check))
                sys.exit(1)
        else: ## If everything checks out, start project
 #               downloading_dependencies()
                commands(SAMPLE,OUTF,ANN,MERGE,FILT)
        subprocess.check_output("rm -r " + TMPDIR, shell=True)
        tprint("\n\n Job Ran Successfully")
        print("\n\n You can see the output files in this directory %s."%OUTF)
end="toilet -f term -F border:gay Thank You for Using MTB-VCF"
subprocess.check_call(end, shell=True)





