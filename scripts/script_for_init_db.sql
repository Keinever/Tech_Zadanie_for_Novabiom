-- Table: public.result_table

-- DROP TABLE IF EXISTS public.result_table;

CREATE TABLE IF NOT EXISTS public.result_table
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 10 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    taxonname text COLLATE pg_catalog."default",
    composition text COLLATE pg_catalog."default",
    change_in_abundance text COLLATE pg_catalog."default",
    frequency text COLLATE pg_catalog."default",
    additive_type text COLLATE pg_catalog."default",
    CONSTRAINT id PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.result_table
    OWNER to admin;

\copy public.result_table(id, taxonname, composition, change_in_abundance, frequency, additive_type) from '/var/lib/postgresql/data/csv_files/result_table.csv' delimiter ',' csv header;