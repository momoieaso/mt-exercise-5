#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/sampled_data
configs=$base/configs

translations=$base/translations

mkdir -p $translations

src=it
trg=en

num_threads=6
device=0

model_name=$1

translations_sub=$translations/$model_name

mkdir -p $translations_sub

# Prepare file to store results
results_file=$translations_sub/results.txt
echo "beam_size,bleu,time" > $results_file

# Loop through different beam sizes
for beam_size in {2..20..2}
do
    SECONDS=0

    # Copy the original config file to a temp file
    tmp_config_file="$configs/${model_name}_beam${beam_size}.yaml"
    cp $configs/$model_name.yaml $tmp_config_file
    
    # Modify the beam_size in the temp config file
    sed -i "s/beam_size: [0-9]*$/beam_size: $beam_size/" $tmp_config_file

    translation_outfile_name=${model_name}_beam${beam_size}
    
    # Perform translation using the modified config file
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python -m joeynmt translate $tmp_config_file < $data/test.$src > $translations_sub/test.$translation_outfile_name.$trg

    # Compute case-sensitive BLEU
    bleu_json=$(cat $translations_sub/test.$translation_outfile_name.$trg | sacrebleu $data/test.$trg --format json)
    bleu_score=$(echo $bleu_json | jq '.score')
    
    # Record time and BLEU score
    echo "$beam_size,$bleu_score,$SECONDS" >> $results_file

    echo "###############################################################################"
    echo "model name: $model_name"
    echo "beam size: $beam_size"
    echo "BLEU: $bleu_score"
    echo "time taken: $SECONDS seconds"
    echo "###############################################################################"
done
