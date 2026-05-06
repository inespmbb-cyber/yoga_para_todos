import sqlite3

def popular_base_de_dados():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # 1. RESET DA TABELA
    cursor.execute("DROP TABLE IF EXISTS posturas")
    cursor.execute('''
        CREATE TABLE posturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            nome_sanscrito TEXT,
            nivel TEXT,
            fase_aula TEXT,
            contraindicacoes TEXT,
            desc_curta TEXT,
            instrucoes TEXT
        )
    ''')

    # 2. LISTA DE 30 POSTURAS
    posturas = [
        # --- AQUECIMENTO ---
        ('Postura do Gato-Vaca (Marjaryasana-Bitilasana)', 'Marjaryasana-Bitilasana', 'Iniciante', 'Aquecimento', 'pulsos', 'Mobilidade da coluna e sincronização da respiração.', '1. Coloque-se de gatas com mãos sob os ombros; 2. Inspire, desça o abdómen e olhe para cima; 3. Expire, arredonde as costas e olhe para o umbigo; 4. Sinta o movimento vértebra por vértebra; 5. Repita o fluxo suavemente.'),
        ('Postura da Criança (Balasana)', 'Balasana', 'Iniciante', 'Aquecimento', 'joelhos', 'Repouso profundo e alongamento lombar.', '1. Ajoelhe-se no tapete; 2. Sente-se sobre os calcanhares; 3. Incline o tronco à frente até a testa tocar o chão; 4. Estenda os braços ou relaxe-os ao lado do corpo; 5. Respire profundamente pelas costas.'),
        ('Cachorro Olhando para Baixo (Adho Mukha Svanasana)', 'Adho Mukha Svanasana', 'Iniciante', 'Aquecimento', 'pulsos', 'Alongamento integral da cadeia posterior.', '1. Comece de gatas; 2. Eleve as ancas em direção ao teto; 3. Forme um V invertido; 4. Pressione as mãos firmemente no chão; 5. Tente levar os calcanhares ao tapete enquanto relaxa o pescoço.'),
        ('Saudação ao Sol A (Surya Namaskar A)', 'Surya Namaskar A', 'Intermédio', 'Aquecimento', 'pulsos, costas', 'Sequência dinâmica para aquecimento.', '1. Comece em pé; 2. Inspire e eleve os braços; 3. Expire e incline o tronco à frente; 4. Passe pela prancha e desça em Chaturanga; 5. Finalize com o Cachorro Olhando para Cima e depois para Baixo.'),
        ('Postura da Montanha (Tadasana)', 'Tadasana', 'Iniciante', 'Aquecimento', 'nenhuma', 'Base de alinhamento e consciência corporal.', '1. Una os pés e distribua o peso; 2. Ative as coxas e o abdómen; 3. Rode os ombros para trás; 4. Mantenha o queixo paralelo ao chão; 5. Imagine a coluna a crescer para o teto.'),
        ('Postura da Pinça Sentada (Paschimottanasana)', 'Paschimottanasana', 'Iniciante', 'Aquecimento', 'lombar', 'Alongamento intenso das pernas e costas.', '1. Sente-se com as pernas esticadas; 2. Inspire e eleve os braços; 3. Expire e dobre o tronco à frente; 4. Segure os pés ou canelas; 5. Mantenha a coluna longa e relaxe o rosto.'),
        ('Ângulo Lateral Estendido (Utthita Parsvakonasana)', 'Utthita Parsvakonasana', 'Intermédio', 'Aquecimento', 'ancras', 'Abertura lateral e força nas pernas.', '1. Afaste bem as pernas; 2. Dobre o joelho direito a 90 graus; 3. Apoie o antebraço na coxa; 4. Estenda o braço esquerdo por cima da orelha; 5. Crie uma linha reta do pé à mão.'),
        ('Postura do Triângulo (Trikonasana)', 'Trikonasana', 'Intermédio', 'Aquecimento', 'coluna', 'Alongamento lateral e equilíbrio.', '1. Afaste as pernas; 2. Rode o pé direito para fora; 3. Incline o tronco para o lado; 4. Toque com a mão na canela ou chão; 5. Estenda o outro braço para o teto.'),
        ('Postura do Guerreiro II (Virabhadrasana II)', 'Virabhadrasana II', 'Iniciante', 'Aquecimento', 'nenhuma', 'Foco e fortalecimento muscular.', '1. Afaste as pernas lateralmente; 2. Rode o pé direito e dobre o joelho; 3. Estenda os braços na linha dos ombros; 4. Olhe por cima da mão direita; 5. Mantenha o tronco centralizado.'),
        ('Prancha (Phalakasana)', 'Phalakasana', 'Iniciante', 'Aquecimento', 'pulsos', 'Fortalecimento do core e braços.', '1. Comece de gatas; 2. Estenda as pernas para trás; 3. Mantenha o corpo numa linha reta; 4. Contraia o abdómen e glúteos; 5. Empurre o chão com as mãos.'),

        # --- DESENVOLVIMENTO ---
        ('Postura do Guerreiro I (Virabhadrasana I)', 'Virabhadrasana I', 'Iniciante', 'Desenvolvimento', 'nenhuma', 'Força e estabilidade.', '1. Dê um passo atrás com o pé a 45 graus; 2. Dobre o joelho da frente; 3. Eleve os braços paralelos; 4. Rode as ancas para a frente; 5. Foque o olhar no horizonte.'),
        ('Postura da Árvore (Vrksasana)', 'Vrksasana', 'Iniciante', 'Desenvolvimento', 'nenhuma', 'Equilíbrio e concentração.', '1. Firme o pé no chão; 2. Apoie o outro pé na coxa interna; 3. Evite o joelho; 4. Junte as mãos no peito; 5. Mantenha o olhar fixo num ponto.'),
        ('Postura do Corvo (Bakasana)', 'Bakasana', 'Avançado', 'Desenvolvimento', 'pulsos', 'Equilíbrio sobre os braços.', '1. Agache-se com mãos no chão; 2. Encaixe joelhos nos tríceps; 3. Incline o peso à frente; 4. Retire os pés do chão; 5. Olhe para a frente, não para baixo.'),
        ('Postura do Barco (Navasana)', 'Navasana', 'Intermédio', 'Desenvolvimento', 'lombar', 'Equilíbrio e força abdominal.', '1. Sente-se com joelhos dobrados; 2. Incline o tronco atrás; 3. Eleve as pernas; 4. Estenda os braços ao lado; 5. Mantenha as costas direitas.'),
        ('Postura da Cadeira (Utkatasana)', 'Utkatasana', 'Iniciante', 'Desenvolvimento', 'joelhos', 'Fortalecimento de coxas.', '1. Una os pés; 2. Dobre os joelhos como se fosse sentar; 3. Peso nos calcanhares; 4. Eleve os braços; 5. Mantenha o peito aberto.'),
        ('Guerreiro III (Virabhadrasana III)', 'Virabhadrasana III', 'Avançado', 'Desenvolvimento', 'nenhuma', 'Equilíbrio e força total.', '1. Parta do Guerreiro I; 2. Incline o tronco à frente; 3. Eleve a perna de trás; 4. Forme um T com o corpo; 5. Mantenha as ancas paralelas ao chão.'),
        ('Postura da Meia Lua (Ardha Chandrasana)', 'Ardha Chandrasana', 'Intermédio', 'Desenvolvimento', 'nenhuma', 'Abertura lateral e equilíbrio.', '1. Do Triângulo, leve a mão ao chão à frente do pé; 2. Eleve a perna de trás; 3. Rode o peito para o lado; 4. Estenda o braço livre; 5. Olhe para o lado ou para cima.'),
        ('Postura do Arco (Dhanurasana)', 'Dhanurasana', 'Intermédio', 'Desenvolvimento', 'costas', 'Abertura peitoral e flexibilidade.', '1. Deite-se de barriga para baixo; 2. Dobre os joelhos e agarre os tornozelos; 3. Inspire e chute os pés para trás; 4. Eleve o peito e as coxas; 5. Respire no abdómen.'),
        ('Postura do Camelo (Ustrasana)', 'Ustrasana', 'Intermédio', 'Desenvolvimento', 'pescoço, costas', 'Abertura cardíaca profunda.', '1. Ajoelhe-se; 2. Coloque mãos na zona lombar; 3. Incline-se para trás; 4. Se possível, toque nos calcanhares; 5. Mantenha as ancas empurradas para a frente.'),
        ('Ponte (Setu Bandhasana)', 'Setu Bandhasana', 'Iniciante', 'Desenvolvimento', 'pescoço', 'Fortalecimento lombar e glúteos.', '1. Deite-se de costas; 2. Dobre os joelhos com pés no chão; 3. Eleve as ancas; 4. Entrelace as mãos sob as costas; 5. Pressione os ombros no tapete.'),

        # --- RELAXAMENTO ---
        ('Postura da Cobra (Bhujangasana)', 'Bhujangasana', 'Iniciante', 'Relaxamento', 'lombar', 'Abertura suave do peito.', '1. Deite-se de barriga para baixo; 2. Mãos sob ombros; 3. Pressione pés no chão; 4. Inspire e eleve o peito; 5. Mantenha cotovelos junto ao corpo.'),
        ('Postura da Pomba (Eka Pada Rajakapotasana)', 'Eka Pada Rajakapotasana', 'Intermédio', 'Relaxamento', 'joelhos', 'Abertura de ancas.', '1. Traga o joelho ao pulso; 2. Estenda a perna de trás; 3. Alinhe as ancas; 4. Incline o tronco à frente; 5. Respire na zona de tensão.'),
        ('Postura do Cadáver (Savasana)', 'Savasana', 'Iniciante', 'Relaxamento', 'nenhuma', 'Relaxamento total final.', '1. Deite-se de costas; 2. Afaste pernas e braços; 3. Palmas para cima; 4. Feche os olhos; 5. Solte todo o peso e respire naturalmente.'),
        ('Postura do Arado (Halasana)', 'Halasana', 'Avançado', 'Relaxamento', 'pescoço', 'Alongamento da coluna vertebral.', '1. Deite-se de costas; 2. Eleve as pernas; 3. Leve os pés ao chão atrás da cabeça; 4. Apoie as costas com as mãos; 5. Não mova o pescoço na postura.'),
        ('Postura da Vela (Sarvangasana)', 'Sarvangasana', 'Avançado', 'Relaxamento', 'pescoço', 'Inversão sobre os ombros.', '1. Deite-se de costas; 2. Eleve pernas e tronco; 3. Apoie as costas com as mãos; 4. Aponte os pés para o teto; 5. Mantenha o queixo no peito.'),
        ('Torção Deitada (Supta Matsyendrasana)', 'Supta Matsyendrasana', 'Iniciante', 'Relaxamento', 'coluna', 'Libertação de tensão nas costas.', '1. Deite-se de costas; 2. Traga um joelho ao peito; 3. Cruze-o sobre o corpo; 4. Olhe para o lado oposto; 5. Relaxe os ombros no chão.'),
        ('Postura do Bebé Feliz (Ananda Balasana)', 'Ananda Balasana', 'Iniciante', 'Relaxamento', 'nenhuma', 'Relaxamento de ancas e sacro.', '1. Deite-se de costas; 2. Dobre joelhos ao peito; 3. Agarre a parte externa dos pés; 4. Afaste os joelhos para as axilas; 5. Balance suavemente de um lado para o outro.'),
        ('Postura do Peixe (Matsyasana)', 'Matsyasana', 'Intermédio', 'Relaxamento', 'pescoço', 'Abertura de garganta e peito.', '1. Deite-se de costas; 2. Coloque mãos sob glúteos; 3. Eleve o peito e arqueie as costas; 4. Toque com o topo da cabeça no chão; 5. Mantenha pernas ativas.'),
        ('Postura do Ângulo Ligado (Baddha Konasana)', 'Baddha Konasana', 'Iniciante', 'Relaxamento', 'joelhos', 'Abertura de ancas e calma.', '1. Sente-se; 2. Junte as plantas dos pés; 3. Deixe os joelhos caírem; 4. Segure os pés; 5. Incline o tronco à frente suavemente.'),
        ('Meditação Sentada (Sukhasana)', 'Sukhasana', 'Iniciante', 'Relaxamento', 'nenhuma', 'Quietude mental e fecho.', '1. Sente-se de pernas cruzadas; 2. Coluna direita; 3. Mãos nos joelhos; 4. Feche os olhos; 5. Foque na respiração por alguns minutos.')
    ]

    # 3. INSERÇÃO DOS DADOS
    cursor.executemany('''
        INSERT INTO posturas (titulo, nome_sanscrito, nivel, fase_aula, contraindicacoes, desc_curta, instrucoes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', posturas)

    conn.commit()
    conn.close()
    print(f"Sucesso: {len(posturas)} posturas de yoga inseridas.")

if __name__ == "__main__":
    popular_base_de_dados()