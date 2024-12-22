import os

from jinja2 import Template


class Q:
    def __init__(self, question, answers, correct_answers, answers_i=""):
        # Initialize question text and image
        if isinstance(question, list):
            self.question_text = question[0]
            self.question_img = question[1] if len(question) > 1 else ""
        elif isinstance(question, str):
            self.question_text = question
            self.question_img = ""
        correct_answers_new = correct_answers
        if type(correct_answers)==list:
            pass
        else:
            correct_answers_new = [int(correct_answers)]
        if answers_i:
            answers_i = answers_i.split(',')
            answers_full = []
            for i in range(len(answers_i)):
                answers_full.append([answers[i], answers_i[i], 1 if i+1 in correct_answers_new else 0])  
            self.answers = answers_full
        else:
            answers_full = []
            for i in range(len(answers)):
                answers_full.append([answers[i], "", 1 if (i+1 in correct_answers_new) else 0])  
            self.answers = answers_full  # Handling empty image URLs

# Create Question objects

# Introduction and Descriptive Statistics for Exploring Data
# Load HTML template
phil = []

phil.append(Q(
    "The specificity of the mythological worldview:",
    [
        "The unity of man and the world",
        "Logical representation of the world",
        "Believing in one God",
        "Reasoning and proving",
        "Expressing inner side of the man"
    ],
    [1]
))

phil.append(Q(
    "Philosophical worldview has its own specifics:",
    [
        "based on the logical method of cognition",
        "based on the rational level of knowledge",
        "has its own set of concepts, categories, special terms.",
        "is a system of knowledge",
        "all answers are correct"
    ],
    [5]
))
phil.append(Q(
    "The object of philosophy:",
    [
        "the man and society",
        "the nature and the god",
        "the being and reality",
        "the world and the man",
        "mind and thinking"
    ],
    [4]
))

phil.append(Q(
    "The subject of philosophy is:",
    [
        "the most general laws and patterns of development and functioning of human society, thinking and the universe",
        "The fundamental principles of being",
        "the Arche",
        "the man in the world",
        "space and time"
    ],
    [1]
))
phil.append(Q(
                "The main divisions of philosophy:",
                [
                    "Sociology, culture, myth, religion",
                    "Physics, psychology, chemistry",
                    "Science, art, moral, politics",
                    "Gnoseology, ontology, ethics, aesthetics",
                    "Worldview, religion, mythology"
                ],
                [4]
))

phil.append(Q(
    "Which function doesn’t belong to philosophy:",
    [
        "Worldview",
        "Scientific",
        "Ideological",
        "Critical",
        "Methodological"
    ],
    [2]
))

phil.append(Q(
    "The basic question of philosophy:",
    [
        "What is primary: consciousness or matter?",
        "What is primary: egg or hen?",
        "What is primary: man or nature?",
        "To be or not to be?",
        "What is the essence of life?"
    ],
    [1]
))

phil.append(Q(
    "The other side of the basic question of philosophy:",
    [
        "Relation of thinking to being",
        "Is there the God?",
        "What is the meaning of life?",
        "Who created the man?",
        "What is reality?"
    ],
    [1]
))

phil.append(Q(
    "Solution of the basic question of philosophy:",
    [
        "Gnosticism and agnosticism",
        "Dualism and monism",
        "Materialism and idealism",
        "Naturalism and sociologism",
        "Theism and atheism"
    ],
    [3]
))

phil.append(Q(
    "Solution of the other side of the basic question of philosophy:",
    [
        "Gnosticism and agnosticism",
        "Dualism and monism",
        "Materialism and idealism",
        "Naturalism and sociologism",
        "Theism and atheism"
    ],
    [5]
))

phil.append(Q(
    "Metaphysics in philosophy states:",
    [
        "the world is unreal",
        "the world is flux",
        "the world is static, unchanging",
        "the world is real",
        "the world is complex"
    ],
    [4]
))

phil.append(Q(
    "Dialectics in philosophy states:",
    [
        "the world is unreal",
        "the world is flux",
        "the world is static, unchanging",
        "the world is real",
        "the world is complex"
    ],
    [5]
))

phil.append(Q(
    "Consciousness is state of:",
    [
        "mental",
        "perception",
        "sensation",
        "thinking",
        "feeling"
    ],
    [4]
))

phil.append(Q(
    "The central problem of Consciousness:",
    [
        "Ideality",
        "Reality",
        "Mind and body",
        "Truth",
        "Qualia"
    ],
    [3]
))

phil.append(Q(
    "What does NOT belong to Sensory knowledge?",
    [
        "sensations",
        "perceptions",
        "representations",
        "reasoning",
        "imagination"
    ],
    [4]
))
phil.append(Q(
    "What does NOT belong to Rational knowledge?",
    [
        "concepts",
        "judgments",
        "conclusions",
        "intuition",
        "theories"
    ],
    [4]
))

phil.append(Q(
    "True being according to Plato:",
    [
        "atoms",
        "ideas",
        "things",
        "souls",
        "god"
    ],
    [2]
))

phil.append(Q(
    "Being according to Aristotle:",
    [
        "substance",
        "predicate",
        "quality",
        "quantity",
        "idea"
    ],
    [1]
))

phil.append(Q(
    "Being according to Heidegger:",
    [
        "essence",
        "substance",
        "existence",
        "reality",
        "ideality"
    ],
    [3]
))

phil.append(Q(
    "Human according to Social Darwinism is:",
    [
        "symbolic animal",
        "organism",
        "sentient being",
        "moral being",
        "social being"
    ],
    [5]
))
phil.append(Q(
    "Human according to Marxism:",
    [
        "symbolic animal",
        "organism",
        "sentient being",
        "moral being",
        "social being"
    ],
    [5]
))

phil.append(Q(
    "Human according to Descartes:",
    [
        "symbolic animal",
        "organism",
        "rational being",
        "moral being",
        "social being"
    ],
    [3]
))

phil.append(Q(
    "Moral is an object of study of:",
    [
        "axiology",
        "epistemology",
        "aesthetics",
        "ethics",
        "logics"
    ],
    [4]
))

phil.append(Q(
    "«Things-in itself» by Kant is:",
    [
        "Things we can cognize",
        "Things we cannot cognize",
        "Things existing",
        "Things non-existing",
        "Ideal things"
    ],
    [2]
))

phil.append(Q(
    "Tengrism can be defined as:",
    [
        "Monotheism",
        "Deism",
        "System of beliefs",
        "Philosophy",
        "Theism"
    ],
    [3]
))

phil.append(Q(
    "Shamanism is a form of:",
    [
        "Spiritualism",
        "Totemism",
        "Magic",
        "Mythology",
        "Religion"
    ],
    [5]
))

phil.append(Q(
    "Combination of different Beliefs, Faiths, Thoughts in one Unique Thinking System is called:",
    [
        "Syncretism",
        "Natural philosophy",
        "Science",
        "Mythology",
        "Religion"
    ],
    [1]
))

phil.append(Q(
    "Levy-Bruhl explained this quality by saying that the primitive mentality obeys something he called ‘the law of participation’, which means that thoughts can be joined by connections which having nothing in common with those of our logic. What did he mean?:",
    [
        "Animism",
        "Totemism",
        "Mythology",
        "Magic",
        "Spiritualism"
    ],
    [3]
))
phil.append(Q(
    "Kazakh nomads had various cults and rites. Which one was essential for Kazakh worldview?:",
    [
        "Cult of ancestors",
        "Cult of the Sun",
        "Cult of the fire",
        "Cult of the earth",
        "Cult of the sky"
    ],
    [1]
))

phil.append(Q(
    "What is the name of philosophical system of Marxism?",
    [
        "Objective idealism",
        "Subjective idealism",
        "Mechanical materialism",
        "Dialectical materialism",
        "Metaphysical materialism"
    ],
    [4]
))

phil.append(Q(
    "The central category of Marx’s Historical materialism:",
    [
        "Politics",
        "Economics",
        "Forms of social consciousness",
        "Social-economic formation",
        "Industrial relations"
    ],
    [4]
))

phil.append(Q(
    "Freedom in accordance with the teachings of Baruch Spinoza is:",
    [
        "Human will",
        "God’s will",
        "Human action",
        "Recognized necessity",
        "Natural law"
    ],
    [4]
))

phil.append(Q(
    "In the irrational philosophy of Soren Kierkegaard, the central problem is:",
    [
        "The essence of man",
        "Rational thinking",
        "The problem of truth",
        "Human existence",
        "Knowledge of God"
    ],
    [4]
))
phil.append(Q(
    "Kazakh nomads had various cults and rites. Which one was essential for Kazakh worldview?:",
    [
        "Cult of ancestors",
        "Cult of the Sun",
        "Cult of the fire",
        "Cult of the earth",
        "Cult of the sky"
    ],
    [1]
))

phil.append(Q(
    "What is the name of philosophical system of Marxism?",
    [
        "Objective idealism",
        "Subjective idealism",
        "Mechanical materialism",
        "Dialectical materialism",
        "Metaphysical materialism"
    ],
    [4]
))

phil.append(Q(
    "The central category of Marx’s Historical materialism:",
    [
        "Politics",
        "Economics",
        "Forms of social consciousness",
        "Social-economic formation",
        "Industrial relations"
    ],
    [4]
))

phil.append(Q(
    "Freedom in accordance with the teachings of Baruch Spinoza is:",
    [
        "Human will",
        "God’s will",
        "Human action",
        "Recognized necessity",
        "Natural law"
    ],
    [4]
))

phil.append(Q(
    "In the irrational philosophy of Soren Kierkegaard, the central problem is:",
    [
        "The essence of man",
        "Rational thinking",
        "The problem of truth",
        "Human existence",
        "Knowledge of God"
    ],
    [4]
))
phil.append(Q(
    "The ethical ideal of Nietzsche's philosophy is:",
    [
        "Hedonist",
        "Christian",
        "Muslim",
        "Stoick",
        "Superman"
    ],
    [5]
))

phil.append(Q(
    "The main philosophical categories of Albert Camus:",
    [
        "Being and thinking",
        "Absurdity and rebellion",
        "Existence and non-existence",
        "Essence and existence",
        "Life and death"
    ],
    [2]
))

phil.append(Q(
    "Why does Jean Paul Sartre believe that Existentialism is humanism?",
    [
        "Man is a free creature",
        "Man himself determines his existence",
        "Man loves",
        "Man is a god-like creature",
        "Man creates"
    ],
    [2]
))

phil.append(Q(
    "What layer of the human psyche was discovered by Sigmund Freud?",
    [
        "Thinking",
        "Unconscious",
        "Archetypes",
        "Imagination",
        "Memory"
    ],
    [2]
))

phil.append(Q(
    "What ancient Greek philosopher believed that the main task was self-knowledge:",
    [
        "Plato",
        "Socrates",
        "Aristotle",
        "Thales",
        "Plotinus"
    ],
    [2]
))
phil.append(Q(
    "Translation of word “axiology”:",
    [
        "Study of values.",
        "Cosmo centrism.",
        "Love Theo",
        "Pantheism",
        "Love Humanity."
    ],
    [1]
))

phil.append(Q(
    "“There are only two substances in the beginning of the world – thinking and extended substances (dualism) is from philosophy of…",
    [
        "E.Kant",
        "D.Hume",
        "R.Descartes",
        "J.-P.Sartre",
        "Protagoras"
    ],
    [3]
))

phil.append(Q(
    "Theory of scientific knowledge is called as…",
    [
        "Cognition",
        "Epistemology",
        "Social philosophy",
        "Feeling",
        "Axiology"
    ],
    [2]
))

phil.append(Q(
    "The object of philosophy is:",
    [
        "Cognition process and the place of man in this world",
        "World in whole and the place of man in this world.",
        "Human being.",
        "Truth, unconcealment.",
        "Mind at whole"
    ],
    [2]
))

phil.append(Q(
    "Ethic is:",
    [
        "A study of nature, origin and limits of human cognition",
        "A study of wisdom",
        "A study of morality and moral behaviour",
        "Branch of physics",
        "World religion"
    ],
    [3]
))
phil.append(Q(
    "Aesthetics is:",
    [
        "A study of nature, origin and limits of human cognition",
        "A philosophical study of principles, moral and human behavior",
        "A study of beauty and art",
        "One of the directions of Buddhism",
        "Philosophy as a system"
    ],
    [3]
))

phil.append(Q(
    "The first historical type of outlook that is considered as a system of ancient legends.",
    [
        "Philosophy",
        "Science",
        "Ethics",
        "Mythology",
        "Theology"
    ],
    [4]
))

phil.append(Q(
    "Faith in the supernatural force(-s), which is based on a strong system of moral norms and the special organization of people, is…",
    [
        "Religion",
        "Ontology",
        "Physics",
        "Epicurianism",
        "Substancialism"
    ],
    [1]
))

phil.append(Q(
    "The Socratic ethical rationalism was formulated as",
    [
        "Virtue is religion",
        "Virtue is arts",
        "Virtue is knowledge",
        "Virtue is war",
        "Virtue is interests"
    ],
    [3]
))

phil.append(Q(
    "One of the outstanding French existentialist:",
    [
        "David Hume",
        "Georg Hegel",
        "Albert Camus",
        "Francis Bacon",
        "Martin Heidegger"
    ],
    [3]
))
phil.append(Q(
    "Division to Subjective spirit, Objective spirit, Absolute spirit comes from philosophy of…?",
    [
        "Fichte",
        "Hegel",
        "Kant",
        "Schelling",
        "Marx"
    ],
    [2]
))

phil.append(Q(
    "Ancient eastern philosophy developed mainly in…",
    [
        "India and China",
        "India and Japan",
        "Persia and China",
        "Egypt and China",
        "India and Korea"
    ],
    [1]
))

phil.append(Q(
    "“Act only on that maxim through which you can at the same time will that become a universal law” is...",
    [
        "the Hegel’s Categorical imperative",
        "the Kant’s Categorical imperative",
        "the Kant’s Hypothetical imperative",
        "the Fichte’s Hypothetical imperative",
        "the Hegel’s Hypothetical imperative"
    ],
    [2]
))

phil.append(Q(
    "The famous Descartes’s formula “Cogito, ergo sum” is translated from Latin as",
    [
        "I think, therefore, I have truth",
        "I think, therefore, I have power",
        "I think, therefore, I have faith",
        "I think, therefore, I exist",
        "I think, therefore, I have values"
    ],
    [4]
))

phil.append(Q(
    "Universal law in Indian philosophy, which operates in the past, present and future, is called…",
    [
        "Thinking",
        "Experience",
        "Analysis",
        "Induction",
        "Karma"
    ],
    [5]
))
phil.append(Q(
    "The first Fr.Baconian idol of all human mind is",
    [
        "Cave",
        "Marketplace",
        "Tribe",
        "Theatre",
        "Mind"
    ],
    [3]
))

phil.append(Q(
    "The second Fr.Baconian idol of personal mind is",
    [
        "Cave",
        "Marketplace",
        "Tribe",
        "Theatre",
        "Mind"
    ],
    [1]
))

phil.append(Q(
    "The third Fr.Baconian idol of mind referred to using terms and words is",
    [
        "Cave",
        "Marketplace",
        "Tribe",
        "Theatre",
        "Mind"
    ],
    [2]
))

phil.append(Q(
    "The fourth Fr.Baconian idol of mind referred to authorities is",
    [
        "Cave",
        "Marketplace",
        "Tribe",
        "Theatre",
        "Mind"
    ],
    [4]
))

phil.append(Q(
    "The doctrine about that knowledge is based on experience is:",
    [
        "Empiricism",
        "Rationalism",
        "Agnosticism",
        "Abstract general ideas",
        "Complexity"
    ],
    [1]
))
phil.append(Q(
    "E.Kant’s categorical imperative is about…",
    [
        "There’s no place like home.",
        "The world is round.",
        "Moral problems.",
        "Everybody everywhere is pretty much the same.",
        "Physical problems."
    ],
    [3]
))

phil.append(Q(
    "The translation of the word “philosophy”:",
    [
        "Pantheism",
        "Love of wisdom.",
        "Cosmo centrism.",
        "Love Theo",
        "Love Human"
    ],
    [2]
))

phil.append(Q(
    "The word “Sophist” is translated from Greek as:",
    [
        "Wise man",
        "Warrior",
        "Judge",
        "Man",
        "Thinker"
    ],
    [1]
))

phil.append(Q(
    "He was called «the first teacher»:",
    [
        "Socrates",
        "Aristotle",
        "Plato",
        "Diogenus",
        "Heraclitus"
    ],
    [2]
))

phil.append(Q(
    "What beginning (Arche) did Heraclitus recognize?",
    [
        "Logos (fire)",
        "Virtue",
        "Intelligence",
        "Honor",
        "Pleasure"
    ],
    [1]
))
phil.append(Q(
    "What beginning did Pythagoras recognize?",
    [
        "Numbers",
        "Dialectical argument",
        "Rational instruction",
        "Learning from our mistakes",
        "Breathing"
    ],
    [1]
))

phil.append(Q(
    "A teaching of Aristotle is called as…",
    [
        "Academicism",
        "Peripatetism",
        "Buddhism",
        "Atheism",
        "Pantheism"
    ],
    [2]
))

phil.append(Q(
    "Under the Renaissance human was considered to be as",
    [
        "Man is a political creature.",
        "Man is a thinking being.",
        "Man is a religious being.",
        "Human is a creator, artist, enriched microcosm.",
        "Man is a sinner."
    ],
    [4]
))

phil.append(Q(
    "“I know that I know nothing” was proclaimed by…",
    [
        "Thales",
        "Pythagorus",
        "Democritus",
        "Seneka",
        "Socrates"
    ],
    [5]
))

phil.append(Q(
    "A thinker who formulated 5 proofs of existence of God:",
    [
        "Augustine",
        "Erasmus of Rotterdam.",
        "Thomas Aquinas.",
        "Machiavelli",
        "Abelyar"
    ],
    [3]
))
phil.append(Q(
    "Myth of the Cave was developed by:",
    [
        "Augustine",
        "Erasmus of Rotterdam",
        "Plato",
        "Makiavelli",
        "Abelyar"
    ],
    [3]
))

phil.append(Q(
    "Theocentrism provides that in the center of the universe is…",
    [
        "God",
        "Something mystical",
        "Poetics",
        "Human",
        "Science"
    ],
    [1]
))

phil.append(Q(
    "Defining characteristic of the religious outlook is:",
    [
        "Belief in art of superstitions",
        "Belief in contemptuous attitude to science, the denial of their validity",
        "Belief in wisdom",
        "Belief in the supernatural, otherworldly forces, having the opportunity to influence the course of world events",
        "Belief in denial of human freedom, the belief that all actions originally defined by God"
    ],
    [4]
))

phil.append(Q(
    "One of the main characteristics of the Renaissance is:",
    [
        "Atheism",
        "Theologism",
        "Sociocentrism",
        "Cosmocentrism",
        "Anthropocentrism"
    ],
    [5]
))

phil.append(Q(
    "Creationism is the idea that the world and mankind created by…",
    [
        "God",
        "Something mystical",
        "Poetics",
        "Human",
        "Science"
    ],
    [1]
))
phil.append(Q(
    "Searching human individuality is the specific feature of Philosophy of...",
    [
        "Conventionalism",
        "Life",
        "Existentialism",
        "Rationalism",
        "Conformism"
    ],
    [3]
))

phil.append(Q(
    "The idea that destinies of the world and people are determined by God is…",
    [
        "Freedom",
        "Desire",
        "Canon",
        "Providentialism",
        "Emotions"
    ],
    [4]
))

phil.append(Q(
    "Who offered psychoanalytic theory in human nature?",
    [
        "Leonardo da Vinci",
        "Nikolas of Cusa",
        "Loranzo Valla",
        "Tomaso Campanella",
        "Sigmund Freud"
    ],
    [5]
))

phil.append(Q(
    "“Thus Spoke Zarathustra” is a work of …",
    [
        "R.Descartes",
        "F.Nietzsche",
        "Albert Camus",
        "Karl Marx",
        "Martin Heidegger"
    ],
    [2]
))

phil.append(Q(
    "Branch of philosophy that studies historical knowledge and interpretation of historical process:",
    [
        "Philosophy of history",
        "Logics",
        "Ontology",
        "History of philosophy",
        "Epistemology"
    ],
    [1]
))
phil.append(Q(
    "The definition of social economic formation in materialism was first developed by...",
    [
        "Engels",
        "Stalin",
        "Marx",
        "Rousseau",
        "Lenin"
    ],
    [3]
))

phil.append(Q(
    "Who is the author of the books “Either/or”, “Fear and Trembling”?",
    [
        "Rousseau",
        "Lenin",
        "Kierkegaard",
        "Marx",
        "Sartre"
    ],
    [3]
))

phil.append(Q(
    "Who indicated the difference between conscious and unconscious in human mind?",
    [
        "Plato",
        "Freud",
        "Hume",
        "Marx",
        "Sartre"
    ],
    [2]
))

phil.append(Q(
    "Aesthetical values are:",
    [
        "Love, friendship",
        "Beauty, art, harmony, style",
        "Civil rights",
        "Freedom of word and personality",
        "Social justice"
    ],
    [2]
))

phil.append(Q(
    "“God is dead” said...",
    [
        "F.Nietzsche",
        "Heraclitus",
        "Plato",
        "E.Kant",
        "F.Hegel"
    ],
    [1]
))
phil.append(Q(
    "What are the main founders of philosophy of existentialism:",
    [
        "Camus, Freud, Florensky",
        "Camus, Sartre, Kierkegaard",
        "Sartre, Spengler, Schelling B.Russel.",
        "I.Kant, Freud, Florensky",
        "Russel, Popper, Adler"
    ],
    [2]
))

phil.append(Q(
    "«The man of absurd» according to Albert Camus is one who understands:",
    [
        "Essence of life",
        "Meaning of life",
        "Meaningless of existence",
        "Philosophy",
        "Others"
    ],
    [3]
))

phil.append(Q(
    "«The man of rebellion» according to Albert Camus is one who states:",
    [
        "I think, therefore I exist",
        "I rebel, therefore I exist",
        "I doubt, therefore I exist",
        "I agree, therefore I exist",
        "I argue, therefore I exist"
    ],
    [2]
))

phil.append(Q(
    "«Borderline situations» according to Sartre is the situation when a man becomes aware of:",
    [
        "Purpose of his life",
        "Problems",
        "Conflicts",
        "The meaning of his life",
        "His coming death"
    ],
    [5]
))

phil.append(Q(
    "According to Sartre: man is:",
    [
        "A project of himself",
        "A social animal",
        "Microcosmos",
        "Symbolic animal",
        "God’s project"
    ],
    [1]
))
phil.append(Q(
    "According to Sigmund Freud «Neurotic» is:",
    [
        "A crazy man",
        "A healthy person with neurotic symptoms",
        "A schizophrenic person",
        "An anxious man",
        "A sick person"
    ],
    [2]
))

phil.append(Q(
    "According to Sigmund Freud «The Unconscious» is:",
    [
        "Ego",
        "Super Ego",
        "Id",
        "Other Ego",
        "Animus"
    ],
    [3]
))

phil.append(Q(
    "According to Carl Gustav Jung «Archetypes» are:",
    [
        "Symbols of Individual Unconscious",
        "Dreams",
        "Symbols of Collective Unconscious",
        "Myths",
        "Spirits"
    ],
    [3]
))

phil.append(Q(
    "According to Carl Gustav Jung human behavior is determined by:",
    [
        "Individual unconsciousness",
        "Environment",
        "Education",
        "Parents",
        "Collective unconsciousness"
    ],
    [5]
))

phil.append(Q(
    "According to Sigmund Freud human behavior is determined by three authorities:",
    [
        "Mind, will, desire",
        "Ego, Id, Super Ego",
        "Body, mind, soul",
        "Father, mother, teacher",
        "Nanny, teacher, boss"
    ],
    [2]
))
phil.append(Q(
    "According to S. Kierkegaard the main problem of philosophy is:",
    [
        "Human essence",
        "Human existence",
        "Human origin",
        "Human mind",
        "Human body"
    ],
    [2]
))

phil.append(Q(
    "S. Kierkegaard wanted to understand why:",
    [
        "Man is an animal",
        "Man is social",
        "Man was thrown into the world",
        "Man is evil",
        "Man is kind"
    ],
    [3]
))

phil.append(Q(
    "According to F. Nietzsche human manifests themselves in:",
    [
        "Will to die",
        "Will to live",
        "Will to power",
        "Will to kill",
        "Will to know"
    ],
    [3]
))

phil.append(Q(
    "According to F. Nietzsche, Superman is a person who:",
    [
        "Does not like people",
        "Does not suffer",
        "Does not like moral",
        "Does not die",
        "Does not believe in God"
    ],
    [5]
))

phil.append(Q(
    "Which ones are the typical Kazakh mythological forms?",
    [
        "Totemism and animism",
        "Tengrism and shamanism",
        "Magic and spiritualism",
        "Polytheism and paganism",
        "Pantheism and fetishism"
    ],
    [2]
))
phil.append(Q(
    "Philosophy of Marxism is called:",
    [
        "Metaphysical materialism",
        "Dialectical materialism",
        "Historical materialism",
        "Objective idealism",
        "Subjective materialism"
    ],
    [2]
))

phil.append(Q(
    "Socio-political theory of Marxism is called:",
    [
        "Metaphysical materialism",
        "Dialectical materialism",
        "Historical materialism",
        "Objective idealism",
        "Subjective materialism"
    ],
    [3]
))

phil.append(Q(
    "Philosophical method of Marxism is called:",
    [
        "Metaphysics",
        "Dialectics",
        "Deduction",
        "Induction",
        "Analogy"
    ],
    [2]
))

phil.append(Q(
    "The idea of Communism in Marxism represents:",
    [
        "Class society",
        "Classless society",
        "Perfect society",
        "Free society",
        "Rich society"
    ],
    [2]
))

phil.append(Q(
    "Historical type of societies in Marxism is called:",
    [
        "Basis and superstructure",
        "Social economic formation",
        "Class society",
        "Classless society",
        "Ideal society"
    ],
    [2]
))
phil.append(Q(
    "What is Consciousness?",
    [
        "function of brain",
        "reflection of reality",
        "self-awareness",
        "ideality",
        "all of them"
    ],
    [5]
))

phil.append(Q(
    "Elements of Consciousness according to A. G. Spirkin:",
    [
        "sensual",
        "rational",
        "value",
        "motivation",
        "all of them"
    ],
    [5]
))

phil.append(Q(
    "Which property of consciousness describes the immaterial essence of consciousness?",
    [
        "ideality",
        "intentionality",
        "ideationality",
        "reflection",
        "self-awareness"
    ],
    [1]
))

phil.append(Q(
    "Who is Homo Sapiens?",
    [
        "Man with thinking",
        "Man with feelings",
        "Man with hands",
        "Man with eyes",
        "Man with soul"
    ],
    [1]
))

phil.append(Q(
    "Consciousness according to theory of Dualism:",
    [
        "material substance",
        "ideationality",
        "immaterial substance",
        "reflection",
        "self-awareness"
    ],
    [3]
))
phil.append(Q(
    "Consciousness according to theory of Darwinism:",
    [
        "property of man",
        "ideal property",
        "reflection of man",
        "self-awareness",
        "highest property of brain"
    ],
    [5]
))

phil.append(Q(
    "Consciousness according to theory of Logical behaviorism:",
    [
        "thoughts",
        "speech",
        "acts",
        "instincts",
        "awareness"
    ],
    [3]
))

phil.append(Q(
    "Self-consciousness is the characteristic of consciousness which describes:",
    [
        "intentionality",
        "ideationality",
        "reflection",
        "ideality",
        "self-awareness"
    ],
    [5]
))

phil.append(Q(
    "Language is:",
    [
        "outer side of consciousness",
        "inner side of consciousness",
        "all ideas",
        "reflective organ",
        "self-awareness"
    ],
    [1]
))

phil.append(Q(
    "What is Ontology?",
    [
        "study of mind",
        "study of Being",
        "study of nature",
        "study of god",
        "study of man"
    ],
    [2]
))
phil.append(Q(
    "What the term «metaphysics» means?",
    [
        "Something real",
        "what comes after physics",
        "something unreal",
        "unknowable",
        "knowable"
    ],
    [2]
))

phil.append(Q(
    "What is Being?",
    [
        "real",
        "category for existence",
        "spiritual",
        "mental",
        "related to humans"
    ],
    [2]
))

phil.append(Q(
    "What is the problem of Being?",
    [
        "What is world",
        "what is the essence of the world",
        "what is reality",
        "what is the god",
        "what is the mind"
    ],
    [2]
))

phil.append(Q(
    "What is Substance?",
    [
        "matter",
        "independent entity",
        "spirit",
        "predicates of things",
        "essence of things"
    ],
    [2]
))

phil.append(Q(
    "Who said: «Being is, but there is not non-being»",
    [
        "Socrates",
        "Parmenides",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [2]
))
phil.append(Q(
    "Who said: «If something denotes the essence of a thing, then it makes sense that being for it does not lie in something else»",
    [
        "Socrates",
        "Parmenides",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [3]
))

phil.append(Q(
    "Who said: «Being is One»",
    [
        "Socrates",
        "Parmenides",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [2]
))

phil.append(Q(
    "Who said: «Being is God»",
    [
        "Socrates",
        "Christianity",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [5]
))

phil.append(Q(
    "Who said: «Being is Two»",
    [
        "Socrates",
        "Descartes",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [2]
))

phil.append(Q(
    "Who said: «Being is plural»",
    [
        "Socrates",
        "Leibniz",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [2]
))
phil.append(Q(
    "Who said: «Being is Absolute Idea»",
    [
        "Socrates",
        "Hegel",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [2]
))

phil.append(Q(
    "Who said: «Being is Man»",
    [
        "Socrates",
        "Heidegger",
        "Aristotle",
        "Plato",
        "Plotinus"
    ],
    [2]
))

phil.append(Q(
    "Forms of Being",
    [
        "Natural",
        "All of them",
        "Spiritual",
        "Human",
        "Social"
    ],
    [2]
))

phil.append(Q(
    "What is Matter?",
    [
        "Ideal being",
        "Material being",
        "Spiritual being",
        "Divine being",
        "Social being"
    ],
    [2]
))

phil.append(Q(
    "Attributes of Matter:",
    [
        "Movement",
        "All of them",
        "Time",
        "Space",
        "Reflection"
    ],
    [2]
))
phil.append(Q(
    "Forms of Motion:",
    [
        "physical",
        "all of them",
        "chemical",
        "biological",
        "social"
    ],
    [2]
))

phil.append(Q(
    "What is Development?",
    [
        "Motion from down to up",
        "motion from simple to complex",
        "motion from low to high",
        "motion from left to right",
        "motion from up to down"
    ],
    [2]
))

phil.append(Q(
    "Two concepts of Development:",
    [
        "Regress and progress",
        "methaphysical and dialectical",
        "cyclic and linear",
        "eternal return",
        "stagnation and change"
    ],
    [2]
))

phil.append(Q(
    "Types of space:",
    [
        "wide",
        "Three-dimensional",
        "narrow",
        "virtual",
        "cosmos"
    ],
    [2]
))

phil.append(Q(
    "Types of time:",
    [
        "physical",
        "all of them",
        "psychological",
        "biological",
        "social"
    ],
    [2]
))
phil.append(Q(
    "Philosophical category which describes visible and invisible sides of things:",
    [
        "Content and form",
        "Essence and phenomenon",
        "Cause and effect",
        "Necessity and contingency",
        "Possibility and reality"
    ],
    [2]
))

phil.append(Q(
    "Philosophical category which describes inner and outer side of things:",
    [
        "Content and form",
        "Essence and phenomenon",
        "Cause and effect",
        "Necessity and contingency",
        "Possibility and reality"
    ],
    [1]
))

phil.append(Q(
    "Philosophical category which describes determinism:",
    [
        "Content and form",
        "Essence and phenomenon",
        "Cause and effect",
        "Necessity and contingency",
        "Possibility and reality"
    ],
    [3]
))

phil.append(Q(
    "What is cognition?",
    [
        "Thinking abt smth",
        "mastering knowledge",
        "working on book",
        "imagining of smth",
        "awareness of smth"
    ],
    [2]
))

phil.append(Q(
    "What is knowledge?",
    [
        "books",
        "information",
        "traditions",
        "customs",
        "opinion"
    ],
    [2]
))
phil.append(Q(
    "What is common between Knowledge and Cognition?",
    [
        "They are the same",
        "knowledge is the result of cognitive process",
        "they are different",
        "both are process",
        "cognition needs prior knowledge"
    ],
    [2]
))

phil.append(Q(
    "What is Epistemology?",
    [
        "Theory of knowledge",
        "theory scientific knowledge",
        "theory of technology",
        "theory of methods",
        "theory of philosophical knowledge"
    ],
    [1]
))

phil.append(Q(
    "What is Gnoseology?",
    [
        "Theory of knowledge",
        "theory scientific knowledge",
        "theory of technology",
        "theory of methods",
        "theory of philosophical knowledge"
    ],
    [1]
))

phil.append(Q(
    "What is Gnosticism?",
    [
        "Cognitive pessimism",
        "Cognitive optimism",
        "Cognitive disbelief",
        "Cognitive doubts",
        "Cognitive negation"
    ],
    [5]
))

phil.append(Q(
    "What is Agnosticism?",
    [
        "Cognitive pessimism",
        "Cognitive optimism",
        "Cognitive disbelief",
        "Cognitive doubts",
        "Cognitive negation"
    ],
    [5]
))
phil.append(Q(
    "What is Skepticism?",
    [
        "Cognitive pessimism",
        "Cognitive optimism",
        "Cognitive disbelief",
        "Cognitive doubts",
        "Cognitive negation"
    ],
    [4]
))

phil.append(Q(
    "Which ideas are TRUE according to Descartes «Theory of Ideas»?",
    [
        "Mind ideas",
        "innate ideas",
        "sensory ideas",
        "authorities’ ideas",
        "common sense"
    ],
    [2]
))

phil.append(Q(
    "Who believed that TRUTH can be proved in the process of socio-historical practice?",
    [
        "Hegel",
        "Marx",
        "Kant",
        "Bacon",
        "Locke"
    ],
    [2]
))

phil.append(Q(
    "Who believed that we can cognize only Phenomena?",
    [
        "Hegel",
        "Marx",
        "Kant",
        "Bacon",
        "Locke"
    ],
    [3]
))

phil.append(Q(
    "Type of Cognition based on Conceptual understanding the reality:",
    [
        "ordinary cognition",
        "scientific cognition",
        "practical cognition",
        "artistic cognition",
        "moral cognition"
    ],
    [2]
))
phil.append(Q(
    "Levels of Cognition:",
    [
        "Ordinary and theoretical",
        "sensual and rational",
        "basic and complex",
        "lower and higher",
        "everyday and scientific"
    ],
    [2]
))

phil.append(Q(
    "What is Judgment?",
    [
        "Statement reflecting the things and their properties",
        "logical image that reproduces the essential properties of objects",
        "deduction from several interrelated judgments of a new judgment",
        "comprehend the truth by seeing it clear",
        "integral image of an object in the unity reflected through sensations"
    ],
    [1]
))

phil.append(Q(
    "What is Concept?",
    [
        "Statement reflecting the things and their properties",
        "logical image that reproduces the essential properties of objects",
        "deduction from several interrelated judgments of a new judgment",
        "comprehend the truth by seeing it clear",
        "integral image of an object in the unity reflected through sensations"
    ],
    [2]
))

phil.append(Q(
    "What is Inference?",
    [
        "Statement reflecting the things and their properties",
        "logical image that reproduces the essential properties of objects",
        "deduction from several interrelated judgments of a new judgment",
        "comprehend the truth by seeing it clear",
        "integral image of an object in the unity reflected through sensations"
    ],
    [3]
))

phil.append(Q(
    "What is Intuition?",
    [
        "Statement reflecting the things and their properties",
        "logical image that reproduces the essential properties of objects",
        "deduction from several interrelated judgments of a new judgment",
        "comprehend the truth by seeing it clear",
        "integral image of an object in the unity reflected through sensations"
    ],
    [4]
))
phil.append(Q(
    "What is Truth in Classical sense?",
    [
        "Truth is the correspondence of knowledge to reality;",
        "this is what is confirmed by experience;",
        "is a kind of agreement – a convention;",
        "usefulness of the knowledge gained;",
        "effectiveness of its use in practice."
    ],
    [1]
))

phil.append(Q(
    "What is correct about Fallacy?",
    [
        "Deliberate distortion of truth",
        "is the essential part of the cognitive process",
        "Lie",
        "Is the fail of cognitive process",
        "Ideological essence of cognition"
    ],
    [1]
))

phil.append(Q(
    "Axiology studies:",
    [
        "notions",
        "values",
        "norms",
        "taboos",
        "laws"
    ],
    [2]
))

phil.append(Q(
    "Absolute values:",
    [
        "yin - yang",
        "truth, beauty, good",
        "justice, injustice",
        "God",
        "Human health"
    ],
    [2]
))

phil.append(Q(
    "Classification of values by carrier:",
    [
        "material, spiritual",
        "individual, supra individual",
        "economical, political",
        "social, family",
        "absolute, specific"
    ],
    [2]
))
phil.append(Q(
    "Classification of values by existence:",
    [
        "material, spiritual",
        "individual, supra individual",
        "economical, political",
        "social, family",
        "absolute, specific"
    ],
    [1]
))

phil.append(Q(
    "What is Ethics?",
    [
        "theory of art",
        "theory of morality",
        "theory of society",
        "theory of religion",
        "theory of nature"
    ],
    [2]
))

phil.append(Q(
    "What is Morality?",
    [
        "social regulation form through beauty-ugly",
        "social regulation form through good-bad",
        "social regulation form through justice-injustice",
        "social regulation form through useful-useless",
        "social regulation form through faith-denial"
    ],
    [2]
))

phil.append(Q(
    "Why is Ethics practical science?",
    [
        "It is studied to know what is good",
        "it is studied in order to become virtuous",
        "It is studied to learn what is evil",
        "It is studied to know more",
        "It is studied to get wisdom"
    ],
    [2]
))

phil.append(Q(
    "Difference between Morality and Mores?",
    [
        "No difference",
        "difference between what is Due and what is Real",
        "norms and ideals",
        "good and bad",
        "week and strong"
    ],
    [2]
))
phil.append(Q(
    "Main Christian values:",
    [
        "Pride and humility",
        "faith, hope, love",
        "cupidity and generosity",
        "lust and chastity",
        "true and lie"
    ],
    [2]
))

phil.append(Q(
    "Which one is Stoic principle?",
    [
        "live for pleasure and well-being",
        "focus on what you control",
        "live a complete and fulfilling life",
        "usefulness, practicability, benefit",
        "prudence, courage, justice"
    ],
    [2]
))

phil.append(Q(
    "Which one is Hedonistic principle?",
    [
        "live for pleasure and well-being",
        "focus on what you control",
        "live a complete and fulfilling life",
        "usefulness, practicability, benefit",
        "prudence, courage, justice"
    ],
    [1]
))

phil.append(Q(
    "Which one is Pragmatic principle?",
    [
        "live for pleasure and well-being",
        "focus on what you control",
        "live a complete and fulfilling life",
        "usefulness, practicability, benefit",
        "prudence, courage, justice"
    ],
    [4]
))

phil.append(Q(
    "What is Epicureanism principle?",
    [
        "live for pleasure and well-being",
        "focus on what you control",
        "live a complete and fulfilling life",
        "usefulness, practicability, benefit",
        "prudence, courage, justice"
    ],
    [1]
))
phil.append(Q(
    "What is Eudemonism principle?",
    [
        "live for pleasure and well-being",
        "focus on what you control",
        "live a complete and fulfilling life",
        "usefulness, practicability, benefit",
        "prudence, courage, justice"
    ],
    [3]
))

phil.append(Q(
    "Essence of Art in classical sense:",
    [
        "Art is representation of reality",
        "Art is beauty, truth, good",
        "Art is expression of spiritual world of artist",
        "Art is only fine art",
        "Art is skill and mastery"
    ],
    [2]
))

phil.append(Q(
    "Essence of Art in Renaissance sense:",
    [
        "Art is representation of reality",
        "Art is beauty, truth, good",
        "Art is expression of spiritual world of artist",
        "Art is only fine art",
        "Art is skill and mastery"
    ],
    [1]
))

phil.append(Q(
    "Essence of Art in 17-18 centuries:",
    [
        "Art is representation of reality",
        "Art is beauty, truth, good",
        "Art is expression of spiritual world of artist",
        "Art is only fine art",
        "Art is skill and mastery"
    ],
    [2]
))

phil.append(Q(
    "Essence of Art in contemporary sense:",
    [
        "Art is representation of reality",
        "Art is beauty, truth, good",
        "Art is expression of spiritual world of artist",
        "Art is only fine art",
        "Art is skill and mastery"
    ],
    [3]
))
phil.append(Q(
    "Essence of Art in traditional sense:",
    [
        "Art is representation of reality",
        "Art is beauty, truth, good",
        "Art is expression of spiritual world of artist",
        "Art is only fine art",
        "Art is skill and mastery"
    ],
    [1]
))

phil.append(Q(
    "Aesthetic categories of Nietzsche:",
    [
        "sublimation",
        "Apollonian and Dionysian",
        "absurd",
        "mimesis",
        "catharsis"
    ],
    [2]
))

phil.append(Q(
    "Aesthetic categories of Freud:",
    [
        "sublimation",
        "Apollonian and Dionysian",
        "absurd",
        "mimesis",
        "catharsis"
    ],
    [1]
))

phil.append(Q(
    "Aesthetic categories of Existentialism:",
    [
        "sublimation",
        "Apollonian and Dionysian",
        "absurd",
        "mimesis",
        "catharsis"
    ],
    [3]
))

phil.append(Q(
    "Aesthetic categories of Plato:",
    [
        "sublimation",
        "Apollonian and Dionysian",
        "absurd",
        "mimesis",
        "catharsis"
    ],
    [4]
))
phil.append(Q(
    "Aesthetic categories of Aristotle:",
    [
        "sublimation",
        "Apollonian and Dionysian",
        "absurd",
        "mimesis",
        "catharsis"
    ],
    [5]
))

phil.append(Q(
    "Whose statement is this? – People are born free or slaves.",
    [
        "Erasmus",
        "Aristotle",
        "Spinoza",
        "Rousseau",
        "Fromm"
    ],
    [2]
))

phil.append(Q(
    "Whose statement is this? – Freedom is human illusion.",
    [
        "Erasmus",
        "Aristotle",
        "Spinoza",
        "Rousseau",
        "Fromm"
    ],
    [3]
))

phil.append(Q(
    "Whose statement is this? – Freedom is realized necessity.",
    [
        "Erasmus",
        "Aristotle",
        "Spinoza",
        "Rousseau",
        "Fromm"
    ],
    [3]
))

phil.append(Q(
    "Whose statement is this? – Freedom is democracy and equality.",
    [
        "Erasmus",
        "Aristotle",
        "Spinoza",
        "Rousseau",
        "Fromm"
    ],
    [4]
))
phil.append(Q(
    "Whose statement is this? – There is freedom from and freedom for.",
    [
        "Erasmus",
        "Aristotle",
        "Spinoza",
        "Rousseau",
        "Fromm"
    ],
    [5]
))

phil.append(Q(
    "Which one describes inevitable course of things which are unavoidable:",
    [
        "liberalism",
        "fatalism",
        "determinism",
        "voluntarism",
        "providentialism"
    ],
    [2]
))

phil.append(Q(
    "Which one describes individual, civil rights, free enterprise:",
    [
        "liberalism",
        "fatalism",
        "determinism",
        "voluntarism",
        "providentialism"
    ],
    [1]
))

phil.append(Q(
    "Which one describes that everything happens due to the objective laws:",
    [
        "liberalism",
        "fatalism",
        "determinism",
        "voluntarism",
        "providentialism"
    ],
    [3]
))

phil.append(Q(
    "Which one describes that everything happens due to somebody’s will:",
    [
        "liberalism",
        "fatalism",
        "determinism",
        "voluntarism",
        "providentialism"
    ],
    [4]
))
phil.append(Q(
    "Which one describes that everything happens due to God’s will:",
    [
        "liberalism",
        "fatalism",
        "determinism",
        "voluntarism",
        "providentialism"
    ],
    [5]
))

phil.append(Q(
    "Tick the criteria of society:",
    [
        "territory",
        "all of them",
        "self-regulation",
        "self-control",
        "integrity"
    ],
    [2]
))

phil.append(Q(
    "What is society?",
    [
        "Aggregate of individuals",
        "Social system",
        "community",
        "social relations",
        "social groups"
    ],
    [1]
))

phil.append(Q(
    "Which definition of society is of Social Darwinism?",
    [
        "Society is social relations",
        "society is organism",
        "Society is geographic adaptation",
        "Society is ideal place",
        "Society is summation of individuals"
    ],
    [2]
))

phil.append(Q(
    "Which definition of society is of Marxism?",
    [
        "Society is social relations",
        "society is organism",
        "Society is geographic adaptation",
        "Society is ideal place",
        "Society is summation of individuals"
    ],
    [1]
))
phil.append(Q(
    "Which definition of society is of Naturalism?",
    [
        "Society is social relations",
        "society is organism",
        "Society is geographic adaptation",
        "Society is ideal place",
        "Society is summation of individuals"
    ],
    [2]
))

phil.append(Q(
    "Which definition of society is of Utopian?",
    [
        "Society is social relations",
        "society is organism",
        "Society is geographic adaptation",
        "Society is ideal place",
        "Society is summation of individuals"
    ],
    [4]
))

phil.append(Q(
    "Which definition of society is of Atomism?",
    [
        "Society is social relations",
        "society is organism",
        "Society is geographic adaptation",
        "Society is ideal place",
        "Society is summation of individuals"
    ],
    [5]
))

phil.append(Q(
    "Which one is concise definition of Culture?",
    [
        "Scope of arts",
        "is material and spiritual environment created by man",
        "life style",
        "fine manners",
        "customs and traditions"
    ],
    [2]
))

phil.append(Q(
    "What are the main characteristics of a Mass Man according to Ortega y Gasset?",
    [
        "responsibility",
        "consumerism",
        "education",
        "high standards",
        "hard work"
    ],
    [2]
))
questions = [*phil]
print(len(questions))
current_dir = os.path.dirname(__file__) if "__file__" in locals() else ""
template_file = os.path.join(current_dir, "index.html")
with open(template_file, "r") as f:
    html_template = f.read()

# Create Jinja template
template = Template(html_template)

# Render HTML codey
html_output = template.render(questions=questions)

# Define the path to the output HTML file
output_file = os.path.join(current_dir, "index_new.html")

# Save HTML code to a file
with open(output_file, "w") as f:
    f.write(html_output)

print("HTML файл успешно сохранен как index_new.html")
