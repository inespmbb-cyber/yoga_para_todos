import sqlite3
import os

def popular_base_de_dados():
    # Garante que o banco de dados seja criado na raiz do projeto (um nível acima da pasta backups)
    caminho_db = os.path.join(os.path.dirname(__file__), '..', 'database.db')
    
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    # 1. RESET DA TABELA
    cursor.execute("DROP TABLE IF EXISTS posturas")
    cursor.execute('''
        CREATE TABLE posturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            instrucoes TEXT,
            nivel TEXT,
            contraindicacoes TEXT,
            fase_aula TEXT
        )
    ''')

    # 2. LISTA DE POSTURAS
    posturas = [
    # --- AQUECIMENTO (Sentado/Chão - Início da Aula) ---
    ('Postura Fácil (Sukhasana)', 'Promover a estabilidade física e mental, preparando o corpo para a meditação.', '1. Sente-se no chão com as pernas cruzadas de forma confortável; 2. Alonge a coluna vertebral em direção ao teto; 3. Repouse as mãos sobre os joelhos com as palmas para cima; 4. Feche os olhos e foque na respiração profunda.', 'Iniciante', 'Joelhos', 'Aquecimento'),
    ('Postura da Criança (Balasana)', 'Acalmar o sistema nervoso, aliviar o stress e alongar suavemente a região lombar.', '1. Ajoelhe-se no tapete e sente-se sobre os calcanhares; 2. Incline o tronco para a frente até a testa tocar o chão; 3. Estenda os braços para a frente ou coloque-os ao longo do corpo; 4. Relaxe os ombros e respire nas costas.', 'Iniciante', 'Joelhos', 'Aquecimento'),
    ('Gato-Vaca (Marjaryasana)', 'Mobilizar a coluna vertebral e coordenar o movimento com o ritmo respiratório.', '1. Comece em posição de quatro apoios; 2. Ao inspirar, deixe a barriga cair e olhe para o teto (Vaca); 3. Ao expirar, empurre o chão e arredonde as costas (Gato); 4. Sincronize o movimento com o ritmo da sua respiração.', 'Iniciante', 'Pulsos', 'Aquecimento'),
    ('Libertação de Ventos (Pawanmuktasana)', 'Melhorar a função digestiva e aliviar a pressão na base da coluna.', '1. Deite-se de costas no chão; 2. Dobre os joelhos e traga-os em direção ao peito; 3. Entrelace os braços ao redor das pernas; 4. Pressione suavemente as coxas contra o abdómen enquanto relaxa o pescoço.', 'Iniciante', 'Lombar', 'Aquecimento'),
    ('Postura do Fio na Agulha (Parsva Balasana)', 'Alongar profundamente os ombros e aliviar a tensão na parte superior das costas.', '1. Comece em quatro apoios; 2. Deslize o braço direito por baixo do tronco até o ombro tocar o chão; 3. Relaxe o lado direito da cabeça no tapete; 4. Mantenha o quadril elevado e sinta o alongamento nas omoplatas.', 'Iniciante', 'Ombros', 'Aquecimento'),
    ('Alongamento de Gato (Uttana Shishosana)', 'Abrir a região torácica e melhorar a mobilidade dos ombros.', '1. Comece em quatro apoios; 2. Caminhe com as mãos para a frente mantendo o quadril sobre os joelhos; 3. Baixe o peito e a testa em direção ao chão; 4. Estique bem os braços para abrir as axilas e ombros.', 'Iniciante', 'Ombros', 'Aquecimento'),
    ('Postura da Borboleta (Baddha Konasana)', 'Aumentar a flexibilidade das virilhas e estimular os órgãos pélvicos.', '1. Sente-se com as pernas à frente; 2. Dobre os joelhos e junte as solas dos pés; 3. Segure os pés e alongue a coluna para cima; 4. Deixe os joelhos caírem para os lados sem forçar.', 'Iniciante', 'Virilha', 'Aquecimento'),

    # --- DESENVOLVIMENTO (Em pé / Força / Equilíbrio - Ativação) ---
    ('Cachorro Olhando para Baixo (Adho Mukha Svanasana)', 'Fortalecer os braços e alongar toda a cadeia posterior (costas e pernas).', '1. Comece de quatro apoios; 2. Levante o quadril em direção ao teto formando um V invertido; 3. Empurre os calcanhares para o chão; 4. Estenda bem os braços e relaxe o pescoço entre os ombros.', 'Iniciante', 'Pulsos', 'Desenvolvimento'),
    ('Guerreiro I (Virabhadrasana I)', 'Fortalecer as pernas e glúteos, expandindo a capacidade respiratória do peito.', '1. Dê um passo largo à frente com o pé direito; 2. Rode o pé de trás para fora a 45 graus; 3. Flexione o joelho da frente a 90 graus; 4. Eleve os braços para o céu unindo as palmas; 5. Mantenha o tronco virado para a frente.', 'Iniciante', 'Joelho', 'Desenvolvimento'),
    ('Guerreiro II (Virabhadrasana II)', 'Desenvolver força física e resistência, enquanto abre os quadris e ombros.', '1. Afaste bem as pernas lateralmente; 2. Rode o pé direito 90 graus para fora; 3. Dobre o joelho direito alinhado com o tornozelo; 4. Estenda os braços horizontalmente; 5. Olhe por cima da mão direita.', 'Iniciante', 'Quadril', 'Desenvolvimento'),
    ('Postura da Árvore (Vrksasana)', 'Melhorar o equilíbrio e a concentração mental, fortalecendo a perna de apoio.', '1. Fique em pé e transfira o peso para a perna esquerda; 2. Coloque a planta do pé direito na coxa ou panturrilha esquerda (evite o joelho); 3. Junte as mãos em prece no peito; 4. Fixe o olhar num ponto à frente para manter o equilíbrio.', 'Iniciante', 'Equilíbrio', 'Desenvolvimento'),
    ('Postura da Montanha (Tadasana)', 'Melhorar a consciência corporal e o alinhamento da coluna vertebral em pé.', '1. Fique em pé com os pés juntos; 2. Distribua o peso uniformemente nas plantas dos pés; 3. Ative as pernas e alongue a coluna; 4. Deixe os braços ao longo do corpo com as palmas para a frente; 5. Mantenha o olhar no horizonte.', 'Iniciante', None, 'Desenvolvimento'),
    ('Postura da Cobra (Bhujangasana)', 'Fortalecer a musculatura lombar e aumentar a flexibilidade da coluna.', '1. Deite-se de barriga para baixo com as mãos sob os ombros; 2. Pressione o peito do pé no chão; 3. Use a força das costas para elevar o peito; 4. Mantenha os cotovelos próximos ao tronco; 5. Olhe suavemente para a frente.', 'Iniciante', 'Lombar', 'Desenvolvimento'),
    ('Postura da Ponte (Setu Bandhasana)', 'Alongar o peito e pescoço enquanto fortalece as pernas e a região lombar.', '1. Deite-se de costas com joelhos dobrados e pés no chão; 2. Coloque os braços ao lado do corpo; 3. Pressione os pés e eleve o quadril em direção ao teto; 4. Tente entrelaçar as mãos sob as costas; 5. Mantenha as coxas paralelas entre si.', 'Iniciante', 'Pescoço', 'Desenvolvimento'),
    ('Postura da Cadeira (Utkatasana)', 'Fortalecer intensamente as coxas e o core, aumentando a energia corporal.', '1. Comece em pé com os pés juntos; 2. Flexione os joelhos como se fosse sentar numa cadeira invisível; 3. Eleve os braços ao lado das orelhas; 4. Mantenha o peso nos calcanhares e o peito aberto.', 'Iniciante', 'Joelhos', 'Desenvolvimento'),
    ('Postura do Triângulo (Trikonasana)', 'Alongar as pernas e a coluna lateralmente, estimulando os órgãos abdominais.', '1. Afaste as pernas lateralmente e rode o pé direito 90 graus; 2. Incline o tronco para a direita mantendo o corpo no mesmo plano; 3. Coloque a mão direita na canela ou no chão; 4. Estenda o braço esquerdo para o teto e olhe para cima.', 'Iniciante', 'Coluna', 'Desenvolvimento'),
    ('Prancha (Phalakasana)', 'Desenvolver força total do corpo, especialmente no abdómen e braços.', '1. Parta de quatro apoios; 2. Estenda as pernas para trás apoiando-se nos dedos dos pés; 3. Mantenha o corpo numa linha reta da cabeça aos calcanhares; 4. Ative bem o abdómen e empurre o chão com as mãos.', 'Intermédio', 'Pulsos', 'Desenvolvimento'),
    ('Postura da Meia Lua (Ardha Chandrasana)', 'Desafiar a coordenação e o equilíbrio lateral enquanto abre o peito.', '1. Comece na postura do triângulo; 2. Coloque a mão direita no chão à frente do pé direito; 3. Eleve a perna esquerda paralelamente ao chão; 4. Rode o tronco para a esquerda e estenda o braço esquerdo para cima.', 'Intermédio', 'Equilíbrio', 'Desenvolvimento'),
    ('Postura da Pinça (Paschimottanasana)', 'Acalmar a mente e alongar profundamente toda a parte posterior do corpo.', '1. Sente-se with as pernas esticadas à frente; 2. Inspire e eleve os braços; 3. Expire e incline o tronco à frente a partir do quadril; 4. Tente segurar os pés ou canelas mantendo a coluna o mais reta possível.', 'Iniciante', 'Lombar', 'Desenvolvimento'),
    ('Postura do Guerreiro III (Virabhadrasana III)', 'Fortalecer a perna de apoio e as costas, desenvolvendo equilíbrio horizontal.', '1. Comece em pé; 2. Incline o tronco para a frente enquanto eleva uma perna para trás; 3. Mantenha o tronco e a perna elevada paralelos ao chão (forma de T); 4. Estenda os braços para a frente para maior desafio.', 'Avançado', 'Equilíbrio', 'Desenvolvimento'),
    ('Postura do Barco (Navasana)', 'Fortalecer os músculos abdominais profundos e os flexores do quadril.', '1. Sente-se com os joelhos dobrados; 2. Incline o tronco ligeiramente para trás e tire os pés do chão; 3. Estenda as pernas formando um V com o corpo; 4. Estenda os braços para a frente e mantenha o peito aberto.', 'Intermédio', 'Lombar', 'Desenvolvimento'),
    ('Cachorro Olhando para Cima (Urdhva Mukha Svanasana)', 'Expandir a caixa torácica e fortalecer os punhos, ombros e coluna.', '1. Deite-se de barriga para baixo; 2. Coloque as mãos ao lado das costelas; 3. Estique os braços e eleve o tronco e as coxas do chão; 4. Apoie-se apenas nas mãos e no peito do pé enquanto abre o peito.', 'Intermédio', 'Pulsos', 'Desenvolvimento'),
    ('Postura do Camelo (Ustrasana)', 'Aumentar a flexibilidade da coluna anterior e aliviar o stress postural.', '1. Ajoelhe-se com as pernas na largura do quadril; 2. Coloque as mãos na lombar; 3. Incline o tronco para trás e tente tocar nos calcanhares; 4. Empurre o quadril para a frente e abra bem o coração.', 'Intermédio', 'Lombar', 'Desenvolvimento'),
    ('Postura da Guirlanda (Malasana)', 'Aliviar a tensão nos quadris e fortalecer os tornozelos e pernas.', '1. Fique em pé com os pés mais largos que o quadril; 2. Flexione os joelhos e agache profundamente; 3. Coloque os cotovelos por dentro dos joelhos; 4. Junte as mãos em prece e use os braços para afastar suavemente os joelhos.', 'Iniciante', 'Joelhos', 'Desenvolvimento'),
    ('Postura do Pombo (Eka Pada Rajakapotasana)', 'Libertar a tensão emocional e física acumulada na região das ancas.', '1. De quatro apoios, traga o joelho direito para trás do pulso direito; 2. Estenda a perna esquerda totalmente para trás; 3. Alinhe o quadril; 4. Se possível, incline o tronco sobre a perna da frente para relaxar.', 'Intermédio', 'Joelhos', 'Desenvolvimento'),

    # --- RELAXAMENTO (Chão / Calma - Finalização) ---
    ('Torção Espinal Deitada (Supta Matsyendrasana)', 'Neutralizar a coluna após a prática e libertar tensões na região abdominal.', '1. Deite-se de costas; 2. Traga o joelho direito ao peito e deixe-o cair para o lado esquerdo; 3. Estenda o braço direito para o lado; 4. Olhe para a mão direita e mantenha os ombros no chão.', 'Iniciante', 'Coluna', 'Relaxamento'),
    ('Postura do Bebé Feliz (Ananda Balasana)', 'Promover o relaxamento sacral e massajar as costas contra o chão.', '1. Deite-se de costas; 2. Traga os joelhos em direção às axilas; 3. Segure as bordas externas dos pés com as mãos; 4. Balance suavemente de um lado para o outro massageando a lombar.', 'Iniciante', None, 'Relaxamento'),
    ('Postura do Arado (Halasana)', 'Acalmar o sistema nervoso central e alongar profundamente a coluna cervical.', '1. Deite-se de costas com braços ao lado do corpo; 2. Eleve as pernas e o quadril levando os pés para trás da cabeça; 3. Tente tocar o chão com os dedos dos pés; 4. Mantenha o pescoço imóvel durante a postura.', 'Intermédio', 'Pescoço', 'Relaxamento'),
    ('Pernas na Parede (Viparita Karani)', 'Restaurar a circulação das pernas e induzir um estado de calma profunda.', '1. Sente-se de lado encostado a uma parede; 2. Deite-se de costas enquanto gira as pernas para cima na parede; 3. Encoste o quadril à parede; 4. Abra os braços e relaxe por alguns minutos.', 'Iniciante', None, 'Relaxamento'),
    ('Postura da Borboleta Deitada (Supta Baddha Konasana)', 'Abrir o peito e o quadril de forma passiva para relaxamento total.', '1. Deite-se de costas; 2. Junte as solas dos pés e deixe os joelhos caírem para os lados; 3. Coloque uma mão no coração e outra na barriga; 4. Respire calmamente sentindo a abertura suave.', 'Iniciante', 'Quadril', 'Relaxamento'),
    ('Postura do Cadáver (Savasana)', 'Absorver conscientemente os benefícios físicos e mentais de toda a prática.', '1. Deite-se de costas no chão; 2. Afaste ligeiramente as pernas e deixe os pés caírem para fora; 3. Afaste os braços do corpo com as palmas para cima; 4. Feche os olhos, relaxe a mandíbula e entregue o peso do corpo.', 'Iniciante', None, 'Relaxamento')
]

    # 3. INSERÇÃO DOS DADOS
    cursor.executemany('''
        INSERT INTO posturas (titulo, descricao, instrucoes, nivel, contraindicacoes, fase_aula)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', posturas)

    conn.commit()
    conn.close()
    print(f"✅ Sucesso: {len(posturas)} posturas de yoga inseridas.")
    print(f"📍 Banco de dados atualizado em: {os.path.abspath(caminho_db)}")

if __name__ == "__main__":
    popular_base_de_dados()