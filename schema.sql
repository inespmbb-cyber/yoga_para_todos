-- Apagar tabelas se existirem para evitar erros ao reiniciar
DROP TABLE IF EXISTS posturas;
DROP TABLE IF EXISTS categorias;

CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE posturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    instrucoes TEXT NOT NULL,
    beneficios TEXT,
    contraindicacoes TEXT,
    nivel TEXT CHECK(nivel IN ('Iniciante', 'Intermédio', 'Avançado')),
    duracao_estimada INTEGER,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias (id)
);