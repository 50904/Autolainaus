
CREATE TABLE public.auto (
                rekisterinumero VARCHAR(7) NOT NULL,
                merkki VARCHAR(30) NOT NULL,
                malli VARCHAR(20) NOT NULL,
                vuosimalli CHAR(4) NOT NULL,
                CONSTRAINT auto_pk PRIMARY KEY (rekisterinumero)
);
COMMENT ON TABLE public.auto IS 'Ajoneuvon perustiedot';


CREATE TABLE public.ryhma (
                ryhma VARCHAR(50) NOT NULL,
                vastuuhenkilo VARCHAR(50),
                CONSTRAINT ryhma_pk PRIMARY KEY (ryhma)
);
COMMENT ON TABLE public.ryhma IS 'Opikelijan luokka';
COMMENT ON COLUMN public.ryhma.ryhma IS 'Ryhmän nimi, esim. auto22B tai henkilökunta';
COMMENT ON COLUMN public.ryhma.vastuuhenkilo IS 'Vastuuopettaja tai lähiesimies';


CREATE TABLE public.lainaaja (
                hetu CHAR(11) NOT NULL,
                sahkoposti VARCHAR(30),
                etunimi VARCHAR(50) NOT NULL,
                sukunimi VARCHAR(50) NOT NULL,
                ryhma VARCHAR(50) NOT NULL,
                ajokorttiluokka VARCHAR(6) NOT NULL,
                CONSTRAINT lainaaja_pk PRIMARY KEY (hetu)
);
COMMENT ON TABLE public.lainaaja IS 'Lainaajan (opiskelija tai ope)
perustiedot';
COMMENT ON COLUMN public.lainaaja.hetu IS 'Kansallinen henkilötunnus';
COMMENT ON COLUMN public.lainaaja.sahkoposti IS 'Rasekon sähköpostiosoite';
COMMENT ON COLUMN public.lainaaja.ryhma IS 'Ryhmän nimi, esim. auto22B tai henkilökunta';
COMMENT ON COLUMN public.lainaaja.ajokorttiluokka IS 'Esim AB TAI ABCE';


CREATE SEQUENCE public.lainaus_lainausnumero_seq;

CREATE TABLE public.lainaus (
                lainausnumero INTEGER NOT NULL DEFAULT nextval('public.lainaus_lainausnumero_seq'),
                hetu CHAR(11) NOT NULL,
                rekisterinumero VARCHAR(7) NOT NULL,
                lainausaika TIMESTAMP NOT NULL,
                palautus TIMESTAMP,
                CONSTRAINT lainaus_pk PRIMARY KEY (lainausnumero)
);
COMMENT ON TABLE public.lainaus IS 'Lainaustapahtuman tiedot';
COMMENT ON COLUMN public.lainaus.lainausnumero IS 'Lainustapahtumalle automaattisesti annettava juokseva numero';
COMMENT ON COLUMN public.lainaus.hetu IS 'Kansallinen henkilötunnus';
COMMENT ON COLUMN public.lainaus.lainausaika IS 'Päivämäärä ja kellonaika, kun auto on otettu lainaana';
COMMENT ON COLUMN public.lainaus.palautus IS 'Palautuksen päivä ja kellonaika';


ALTER SEQUENCE public.lainaus_lainausnumero_seq OWNED BY public.lainaus.lainausnumero;

ALTER TABLE public.lainaus ADD CONSTRAINT auto_lainaus_fk
FOREIGN KEY (rekisterinumero)
REFERENCES public.auto (rekisterinumero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.lainaaja ADD CONSTRAINT ryhma_lainaaja_fk
FOREIGN KEY (ryhma)
REFERENCES public.ryhma (ryhma)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.lainaus ADD CONSTRAINT lainaaja_lainaus_fk
FOREIGN KEY (hetu)
REFERENCES public.lainaaja (hetu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
