## MTB-VCF - Mycobacterium Tuberculosis targeted Varaint calling pipeline!

**What is MTB-VCF?** <br>
<p align = "justify">
<br> MTB-VCF - It is a multipurpose tool for targeted variant calling of genetic polymorphisms in Mycobacterium Tuberculosis. It is a Python-based command line Variant Calling pipeline, designed to streamline the batch processing of samples with a single command line which takes raw reads (FastQ) files as the input. The pipeline currently targets four anti-tuberculosis drug genes (rpoB, rpsl, katG, inhA, aphC) and has been tested on 2221 isolates of Mycobacterium tuberculosis to evaluate its predictive performance compared with DST data. The specificity and sensitivity of the pipeline were also assessed by comparing the results to those obtained using TBProfiler and KVARQ. Utilizing DST as the reference standard, the MTB-VCF pipeline demonstrated sensitivities of 99% for detecting multi-drug-resistant TB (MDR), 96% for pre-extensively drug-resistant TB (Pre-XDR), and 93% for extensively drug-resistant TB (XDR), with corresponding specificities of 98%, 99%, and 96%. The study found that the MTB-VCF pipeline exhibited superior predictive performance compared to TBProfiler and KVARQ, as it did not miss any mutations detected by these pipelines and identified additional mutations across the targeted drugs genes.
Conclusion: The MTB-VCF pipeline demonstrates the ability to rapidly and accurately predict anti-tuberculosis (TB) drug resistance profiles for the provided gene list using whole-genome sequencing (WGS) data across large numbers of samples. The pipeline's computing architecture enables modifications to the core bioinformatic pipelines and outputs, such as analyzing WGS data sourced from portable technologies. The pipeline has the potential to be integrated into point-of-care and WGS diagnostic environments, even in resource-poor settings. <br>
</p>


**MTB-VCF** is written in Python and C, is open-source and published under GNU GPLv3.

 **Hardware specification** 

MTB-VCF runs on Linux system or WSL2-Ubuntu that runs Python v-2.70. Analyses in this study were performed on a Ubuntu Linux Server with four six-core AMD Opteron CPUs and 128 GB RAM, using 8 threads.


 **Installation**
```
python install.py
```
