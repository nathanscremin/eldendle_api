# Our database of Elden Ring bosses
# Data gathered from Fextralife wiki
BOSS_DATABASE = {
    # --- BASE GAME: SHARDBEARERS (MAIN) ---
    "Godrick the Grafted": {
        "nome": "Godrick the Grafted",
        "regiao": "Limgrave",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Humanoid",
        "localizacao_especifica": "Stormveil Castle",
        "drop_principal": "Godrick's Great Rune",
        "obrigatorio": True,
        "runes": 20000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/godrick_the_grafted_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Rennala, Queen of the Full Moon": {
        "nome": "Rennala, Queen of the Full Moon",
        "regiao": "Liurnia of the Lakes",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Humanoid",
        "localizacao_especifica": "Raya Lucaria Academy",
        "drop_principal": "Great Rune of the Unborn",
        "obrigatorio": True,
        "runes": 40000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/rennala_queen_of_the_full_moon_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Starscourge Radahn": {
        "nome": "Starscourge Radahn",
        "regiao": "Caelid",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Humanoid",
        "localizacao_especifica": "Wailing Dunes",
        "drop_principal": "Radahn's Great Rune",
        "obrigatorio": True,
        "runes": 70000, # <-- ADICIONADO (Fonte: Fextralife)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/starscourge_radahn_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Rykard, Lord of Blasphemy": {
        "nome": "Rykard, Lord of Blasphemy",
        "regiao": "Mt. Gelmir",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Serpent",
        "localizacao_especifica": "Volcano Manor",
        "drop_principal": "Rykard's Great Rune",
        "obrigatorio": True,
        "runes": 130000, # <-- ADICIONADO (Fonte: Fextralife)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/rykard_lord_of_blasphemy_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Morgott, the Omen King": {
        "nome": "Morgott, the Omen King",
        "regiao": "Leyndell, Royal Capital",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Omen",
        "localizacao_especifica": "Elden Throne",
        "drop_principal": "Morgott's Great Rune",
        "obrigatorio": True,
        "runes": 120000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/morgott_the_omen_king_boss_elden_ring_wiki_guide_200px.jpg"
    },

    # --- BASE GAME: MAIN STORY (ENDGAME) ---
    "Fire Giant": {
        "nome": "Fire Giant",
        "regiao": "Mountaintops of the Giants",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Giant",
        "localizacao_especifica": "Flame Peak",
        "drop_principal": "Remembrance of the Fire Giant",
        "obrigatorio": True,
        "runes": 180000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/fire_giant_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Maliketh, the Black Blade": {
        "nome": "Maliketh, the Black Blade",
        "regiao": "Crumbling Farum Azula",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Beast",
        "localizacao_especifica": "Beside the Great Bridge",
        "drop_principal": "Remembrance of the Black Blade",
        "obrigatorio": True,
        "runes": 220000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/maliketh_the_black_blade_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Godfrey, First Elden Lord": {
        "nome": "Godfrey, First Elden Lord",
        "regiao": "Leyndell, Ashen Capital",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Humanoid",
        "localizacao_especifica": "Elden Throne",
        "drop_principal": "Remembrance of Hoarah Loux",
        "obrigatorio": True,
        "runes": 300000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/godfrey_first_elden_lord_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Radagon of the Golden Order": {
        "nome": "Radagon of the Golden Order",
        "regiao": "Leyndell, Ashen Capital",
        "fase": 2, 
        "tipo": "God",
        "raca": "God",
        "localizacao_especifica": "Elden Throne",
        "drop_principal": "Elden Remembrance",
        "obrigatorio": True,
        "runes": 500000, # <-- ADICIONADO (Drop do Elden Beast)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/radagon_of_the_golden_order_boss_elden_ring_wiki_guide_200px.jpg"
    },

    # --- BASE GAME: MAJOR OPTIONAL ---
    "Malenia, Blade of Miquella": {
        "nome": "Malenia, Blade of Miquella",
        "regiao": "Miquella's Haligtree",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Empyrean",
        "localizacao_especifica": "Elphael, Brace of the Haligtree",
        "drop_principal": "Malenia's Great Rune",
        "obrigatorio": False,
        "runes": 480000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/malenia_blade_of_miquella_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Mohg, Lord of Blood": {
        "nome": "Mohg, Lord of Blood",
        "regiao": "Mohgwyn Palace",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Omen",
        "localizacao_especifica": "Mohgwyn Dynasty Mausoleum",
        "drop_principal": "Mohg's Great Rune",
        "obrigatorio": False,
        "runes": 420000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/mohg_lord_of_blood_boss_elden_ring_wiki_guide_200px.jpg"
    },

    # --- DLC: SHADOW OF THE ERDTREE (MAIN) ---
    "Divine Beast Dancing Lion": {
        "nome": "Divine Beast Dancing Lion",
        "regiao": "Gravesite Plain",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Beast",
        "localizacao_especifica": "Belurat, Tower Settlement",
        "drop_principal": "Remembrance of the Dancing Lion",
        "obrigatorio": True,
        "runes": 120000, # <-- ADICIONADO (Fonte: Fextralife)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/divine_beast_dancing_lion_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Rellana, Twin Moon Knight": {
        "nome": "Rellana, Twin Moon Knight",
        "regiao": "Scadu Altus",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Humanoid",
        "localizacao_especifica": "Castle Ensis",
        "drop_principal": "Remembrance of the Twin Moon Knight",
        "obrigatorio": True,
        "runes": 240000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/rellana_twin_moon_knight_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Messmer the Impaler": {
        "nome": "Messmer the Impaler",
        "regiao": "Scadu Altus",
        "fase": 2,
        "tipo": "Demigod",
        "raca": "Humanoid",
        "localizacao_especifica": "Shadow Keep",
        "drop_principal": "Remembrance of the Impaler",
        "obrigatorio": True,
        "runes": 400000, # <-- ADICIONADO (Fonte: Fextralife)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/messmer_the_impaler_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Promised Consort Radahn": {
        "nome": "Promised Consort Radahn",
        "regiao": "Enir-Ilim",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Humanoid",
        "localizacao_especifica": "Enir-Ilim",
        "drop_principal": "Remembrance of Radahn, Consort",
        "obrigatorio": True,
        "runes": 500000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/promised_consort_radahn_boss_elden_ring_wiki_guide_200px.jpg"
    },

    # --- BASE GAME: MAJOR OPTIONAL (CONTINUAÇÃO) ---
    "Margit, the Fell Omen": {
        "nome": "Margit, the Fell Omen",
        "regiao": "Limgrave",
        "fase": 1,
        "tipo": "Great Enemy",
        "raca": "Omen",
        "localizacao_especifica": "Stormveil Castle",
        "drop_principal": "Talisman Pouch",
        "obrigatorio": False, 
        "runes": 12000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/margit_the_fell_omen_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Godskin Duo": {
        "nome": "Godskin Duo",
        "regiao": "Crumbling Farum Azula",
        "fase": 1, 
        "tipo": "Legend",
        "raca": "Humanoid",
        "localizacao_especifica": "Dragon Temple",
        "drop_principal": "Smithing-Stone Miner's Bell Bearing [4]",
        "obrigatorio": True, 
        "runes": 170000, # <-- ADICIONADO (Fonte: Fextralife)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/godskin_duo_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Lichdragon Fortissax": {
        "nome": "Lichdragon Fortissax",
        "regiao": "Deeproot Depths",
        "fase": 1,
        "tipo": "Legend",
        "raca": "Dragon",
        "localizacao_especifica": "Prince of Death's Throne",
        "drop_principal": "Remembrance of the Lichdragon",
        "obrigatorio": False, 
        "runes": 90000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/lichdragon_fortissax_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Dragonlord Placidusax": {
        "nome": "Dragonlord Placidusax",
        "regiao": "Crumbling Farum Azula",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Dragon",
        "localizacao_especifica": "Beside the Great Bridge",
        "drop_principal": "Remembrance of the Dragonlord",
        "obrigatorio": False,
        "runes": 280000, # <-- ADICIONADO (Fonte: Fextralife)
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/dragonlord_placidusax_boss_elden_ring_wiki_guide_200px.jpg"
    },

    # --- DLC: SHADOW OF THE ERDTREE (OUTROS PRINCIPAIS/OPCIONAIS) ---
    "Romina, Saint of the Bud": {
        "nome": "Romina, Saint of the Bud",
        "regiao": "Ancient Ruins of Rauh",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Humanoid",
        "localizacao_especifica": "Church of the Bud",
        "drop_principal": "Remembrance of the Saint of the Bud",
        "obrigatorio": True, 
        "runes": 380000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/romina_saint_of_the_bud_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Midra, Lord of Frenzied Flame": {
        "nome": "Midra, Lord of Frenzied Flame",
        "regiao": "Abyssal Woods",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Humanoid",
        "localizacao_especifica": "Midra's Manse",
        "drop_principal": "Remembrance of the Lord of Frenzied Flame",
        "obrigatorio": False,
        "runes": 410000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/midra_lord_of_frenzied_flame_boss_elden_ring_wiki_guide_200px.jpg"
    },
    "Bayle the Dread": {
        "nome": "Bayle the Dread",
        "regiao": "Jagged Peak",
        "fase": 2,
        "tipo": "Legend",
        "raca": "Dragon",
        "localizacao_especifica": "Jagged Peak Summit",
        "drop_principal": "Heart of Bayle",
        "obrigatorio": False,
        "runes": 490000, # <-- ADICIONADO
        "imagem_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/bayle_the_dread_boss_elden_ring_wiki_guide_200px.jpg"
    },
}