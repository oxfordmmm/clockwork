version = 3

tables = {
    'Isolate': [
        ('isolate_id', 'integer'),
        ('sample_id', 'integer'),
        ('isolate_number_from_lab', 'text'),
        ('pool_sequence_replicates', 'integer'),
        ('ena_experiment_accession', 'text'),
    ],

    'Pipeline': [
        ('isolate_id', 'integer'),
        ('seqrep_id', 'integer'),
        ('seqrep_pool', 'text'),
        ('version', 'text'),
        ('pipeline_name', 'text'),
        ('status', 'integer'),
        ('reference_id', 'integer'),
    ],

    'QC': [
        ('seqrep_id', 'integer'),
        ('pipeline_version', 'text'),
        ('fastqc1_gc', 'float'),
        ('fastqc1_adapter_content', 'text'),
        ('fastqc1_basic_statistics', 'text'),
        ('fastqc1_kmer_content', 'text'),
        ('fastqc1_max_sequence_length', 'integer unsigned'),
        ('fastqc1_min_sequence_length', 'integer unsigned'),
        ('fastqc1_overrepresented_sequences', 'text'),
        ('fastqc1_per_base_n_content', 'text'),
        ('fastqc1_per_base_sequence_content', 'text'),
        ('fastqc1_per_base_sequence_quality', 'text'),
        ('fastqc1_per_sequence_gc_content', 'text'),
        ('fastqc1_per_sequence_quality_scores', 'text'),
        ('fastqc1_sequence_duplication_levels', 'text'),
        ('fastqc1_sequence_length_distribution', 'text'),
        ('fastqc1_sequences_flagged_as_poor_quality', 'integer unsigned'),
        ('fastqc1_total_sequences', 'integer unsigned'),
        ('fastqc2_gc', 'float'),
        ('fastqc2_adapter_content', 'text'),
        ('fastqc2_basic_statistics', 'text'),
        ('fastqc2_kmer_content', 'text'),
        ('fastqc2_max_sequence_length', 'integer unsigned'),
        ('fastqc2_min_sequence_length', 'integer unsigned'),
        ('fastqc2_overrepresented_sequences', 'text'),
        ('fastqc2_per_base_n_content', 'text'),
        ('fastqc2_per_base_sequence_content', 'text'),
        ('fastqc2_per_base_sequence_quality', 'text'),
        ('fastqc2_per_sequence_gc_content', 'text'),
        ('fastqc2_per_sequence_quality_scores', 'text'),
        ('fastqc2_sequence_duplication_levels', 'text'),
        ('fastqc2_sequence_length_distribution', 'text'),
        ('fastqc2_sequences_flagged_as_poor_quality', 'integer unsigned'),
        ('fastqc2_total_sequences', 'integer unsigned'),
        ('samtools_raw_total_sequences', 'integer unsigned'),
        ('samtools_reads_mapped', 'integer unsigned'),
        ('samtools_reads_duplicated', 'integer unsigned'),
        ('samtools_bases_mapped_cigar', 'bigint unsigned'),
        ('samtools_bases_trimmed', 'bigint unsigned'),
        ('samtools_error_rate', 'float'),
        ('samtools_average_quality', 'float'),
        ('samtools_insert_size_average', 'float'),
        ('samtools_insert_size_standard_deviation', 'float'),
        ('samtools_inward_oriented_pairs', 'integer unsigned'),
        ('samtools_outward_oriented_pairs', 'integer unsigned'),
        ('samtools_pairs_with_other_orientation', 'integer unsigned'),
        ('het_snp_positions', 'integer unsigned'),
        ('het_snp_total_snps', 'integer unsigned'),
        ('het_snp_het_calls', 'integer unsigned'),
    ],

    'Read_counts': [
        ('seqrep_id', 'integer'),
        ('original_total', 'integer unsigned'),
        ('contamination', 'integer unsigned'),
        ('not_contamination', 'integer unsigned'),
        ('unmapped', 'integer unsigned'),
        ('total_after_remove_contam', 'integer unsigned'),
    ],

    'Reference': [
        ('reference_id', 'integer'),
        ('name', 'text'),
    ],

    'Sample': [
        ('sample_id', 'integer'),
        ('subject_id', 'text'),
        ('site_id', 'text'),
        ('sample_id_from_lab', 'text'),
        ('dataset_name', 'text'),
        ('ena_center_name', 'text'),
        ('ena_sample_accession', 'text'),
        ('ena_study_accession', 'text'),
    ],

    'Seqrep': [
        ('seqrep_id', 'integer'),
        ('isolate_id', 'integer'),
        ('sequence_replicate_number', 'bigint unsigned'),
        ('original_reads_file_1_md5', 'text'),
        ('original_reads_file_2_md5', 'text'),
        ('remove_contam_reads_file_1_md5', 'text'),
        ('remove_contam_reads_file_2_md5', 'text'),
        ('withdrawn', 'integer'),
        ('import_status', 'integer'),
        ('submission_date', 'date'),
        ('submit_to_ena', 'integer'),
        ('instrument_model', 'text'),
        ('ena_run_accession', 'text'),
        ('ena_on_hold', 'integer'),
    ],

    'Version': [
        ('version', 'integer'),
    ]
}


primary_keys = {
    'Isolate': 'isolate_id',
    'Mykrobe_panel': 'mykrobe_panel_id',
    'Reference': 'reference_id',
    'Sample': 'sample_id',
    'Seqrep': 'seqrep_id',
}

