from Objects.wildflower import WildFlower

# Dictionary containing wildflower objects
wildflowers = {
    "New England Aster": WildFlower(
        "New England Aster",
        "Symphyotrichum novae-angliae", 
        "Northeast",
        "4-8",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate", 
            "Frost tolerant": "Yes",
            "Growing season": "Late summer to fall bloom",
            "Description": "Purple daisy-like flowers with yellow centers, 3-6 feet tall",
            "Interesting fact": "One of the last flowers to bloom, providing crucial late-season nectar for migrating monarch butterflies"
        }
    ),
    
    "Wild Bergamot": WildFlower(
        "Wild Bergamot",
        "Monarda fistulosa",
        "Northeast, Southeast, Midwest", 
        "3-9",
        "Non-toxic (edible/medicinal)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "10-14", 
            "Days to maturity": "90-100"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes", 
            "Growing season": "Mid to late summer",
            "Description": "Lavender tubular flowers in clusters, 2-4 feet tall, minty fragrance",
            "Interesting fact": "Native Americans used it as a natural antiseptic and called it 'bee balm'"
        }
    ),
    
    "Purple Coneflower": WildFlower(
        "Purple Coneflower",
        "Echinacea purpurea",
        "Northeast, Southeast, Midwest",
        "3-9", 
        "Non-toxic (medicinal)",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "14-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Summer", 
            "Description": "Purple petals drooping around orange cone center, 2-5 feet tall",
            "Interesting fact": "Seeds provide food for goldfinches throughout winter"
        }
    ),
    
    "Black-Eyed Susan": WildFlower(
        "Black-Eyed Susan",
        "Rudbeckia fulgida",
        "Northeast, Southeast, Midwest",
        "3-9",
        "Mildly toxic to livestock", 
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "7-14",
            "Days to maturity": "80-100"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Summer to early fall",
            "Description": "Bright yellow petals with dark brown center, 1-3 feet tall", 
            "Interesting fact": "Maryland's state flower and extremely long-blooming (up to 8 weeks)"
        }
    ),
    
    "Wild Lupine": WildFlower(
        "Wild Lupine", 
        "Lupinus perennis",
        "Northeast, Midwest",
        "4-8",
        "Toxic (contains alkaloids)",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "14-28",
            "Days to maturity": "365+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate", 
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to early summer",
            "Description": "Blue-purple flower spikes, palmately compound leaves, 1-2 feet tall",
            "Interesting fact": "Only host plant for the endangered Karner Blue butterfly"
        }
    ),
    
    "Wild Columbine": WildFlower(
        "Wild Columbine",
        "Aquilegia canadensis",
        "Northeast, Midwest",
        "3-8",
        "Mildly toxic",
        {
            "Requires light for germination?": "No (needs cold stratification)",
            "Days to germinate": "21-30",
            "Days to maturity": "365+ (blooms second year)"
        },
        {
            "Required sunlight": "Partial shade to full shade",
            "Drought tolerant": "No",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to early summer",
            "Description": "Red and yellow bell-shaped flowers with spurs, 1-2 feet tall",
            "Interesting fact": "Flowers are specifically adapted for hummingbird pollination"
        }
    ),
    
    "Cardinal Flower": WildFlower(
        "Cardinal Flower",
        "Lobelia cardinalis", 
        "Northeast, Southeast",
        "3-9",
        "Toxic (all parts)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Partial shade to full sun",
            "Drought tolerant": "No (prefers moist soil)",
            "Frost tolerant": "Moderate",
            "Growing season": "Mid to late summer",
            "Description": "Brilliant red tubular flowers on tall spikes, 2-4 feet tall",
            "Interesting fact": "One of the few truly red wildflowers in North America"
        }
    ),
    
    "Goldenrod": WildFlower(
        "Goldenrod",
        "Solidago canadensis",
        "Northeast, Southeast", 
        "3-9",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Late summer to fall",
            "Description": "Dense clusters of tiny yellow flowers, 3-5 feet tall",
            "Interesting fact": "Often blamed for hay fever, but ragweed is the real culprit"
        }
    ),
    
    "Wild Ginger": WildFlower(
        "Wild Ginger",
        "Asarum canadense",
        "Northeast",
        "4-8", 
        "Mildly toxic",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "30-60",
            "Days to maturity": "365+ (slow growing)"
        },
        {
            "Required sunlight": "Full shade to partial shade",
            "Drought tolerant": "No",
            "Frost tolerant": "Yes",
            "Growing season": "Early spring (flowers), year-round foliage",
            "Description": "Heart-shaped leaves, small burgundy flowers at ground level",
            "Interesting fact": "Flowers are pollinated by flies and beetles, not bees"
        }
    ),
    
    "Trout Lily": WildFlower(
        "Trout Lily",
        "Erythronium americanum",
        "Northeast",
        "3-8",
        "Non-toxic (edible when cooked)",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "Variable (may take 2+ years)",
            "Days to maturity": "2190+ (7+ years to bloom from seed)"
        },
        {
            "Required sunlight": "Partial shade (spring ephemeral)",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes", 
            "Growing season": "Early spring",
            "Description": "Yellow nodding flowers, mottled leaves, 4-6 inches tall",
            "Interesting fact": "Takes up to 7 years to bloom from seed and forms large colonies through bulb division"
        }
    ),
    
    # Southeast Wildflowers
    "Coral Honeysuckle": WildFlower(
        "Coral Honeysuckle",
        "Lonicera sempervirens",
        "Southeast",
        "4-9",
        "Non-toxic",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "14-30",
            "Days to maturity": "730+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Spring through fall",
            "Description": "Orange-red tubular flowers, climbing vine up to 20 feet",
            "Interesting fact": "Primary nectar source for ruby-throated hummingbirds during migration"
        }
    ),
    
    "Butterfly Weed": WildFlower(
        "Butterfly Weed",
        "Asclepias tuberosa",
        "Southeast",
        "3-9",
        "Mildly toxic (milkweed family)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "7-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Summer",
            "Description": "Bright orange clusters of small flowers, 1-3 feet tall",
            "Interesting fact": "Essential host plant for monarch butterflies and extremely drought tolerant"
        }
    ),
    
    "Wild Bergamot (Southern)": WildFlower(
        "Wild Bergamot (Southern)",
        "Monarda punctata",
        "Southeast",
        "4-9",
        "Non-toxic (medicinal)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "10-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Moderate",
            "Growing season": "Late summer to fall",
            "Description": "Yellow flowers with purple spots, whorl arrangement, 2-4 feet tall",
            "Interesting fact": "Spotted bee balm attracts beneficial insects and has natural antifungal properties"
        }
    ),
    
    "Partridge Pea": WildFlower(
        "Partridge Pea",
        "Chamaecrista fasciculata",
        "Southeast",
        "2-11",
        "Non-toxic",
        {
            "Requires light for germination?": "No (scarification needed)",
            "Days to germinate": "7-14",
            "Days to maturity": "60-90"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Low (annual)",
            "Growing season": "Summer to fall",
            "Description": "Yellow flowers with red centers, compound leaves, 1-3 feet tall",
            "Interesting fact": "Seeds are important food for bobwhite quail and other ground birds"
        }
    ),
    
    "Blazing Star": WildFlower(
        "Blazing Star",
        "Liatris spicata",
        "Northeast, Southeast, Midwest",
        "3-9",
        "Non-toxic",
        {
            "Requires light for germination?": "No (cold stratification helpful)",
            "Days to germinate": "14-30",
            "Days to maturity": "365+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Late summer",
            "Description": "Purple spike flowers blooming from top down, 2-5 feet tall",
            "Interesting fact": "Unusual among flowers for blooming from top to bottom of spike"
        }
    ),
    
    "Wild Ginger (Southern)": WildFlower(
        "Wild Ginger (Southern)",
        "Hexastylis arifolia",
        "Southeast",
        "5-9",
        "Non-toxic",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "30-90",
            "Days to maturity": "730+ (slow growing)"
        },
        {
            "Required sunlight": "Full shade to partial shade",
            "Drought tolerant": "No",
            "Frost tolerant": "Yes",
            "Growing season": "Spring (flowers), evergreen foliage",
            "Description": "Heart-shaped evergreen leaves, small brown flowers at soil level",
            "Interesting fact": "Evergreen groundcover that forms dense colonies in deciduous forests"
        }
    ),
    
    "Coralbean": WildFlower(
        "Coralbean",
        "Erythrina herbacea",
        "Southeast",
        "7-11",
        "Toxic (seeds especially)",
        {
            "Requires light for germination?": "No (scarification needed)",
            "Days to germinate": "14-28",
            "Days to maturity": "730+ (woody perennial)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Low (dies back in winter)",
            "Growing season": "Spring to early summer",
            "Description": "Bright red tubular flowers, compound leaves, 3-6 feet tall",
            "Interesting fact": "Hummingbird magnet with brilliant red seeds used in Native American jewelry"
        }
    ),
    
    "Carolina Wild Petunia": WildFlower(
        "Carolina Wild Petunia",
        "Ruellia caroliniensis",
        "Southeast",
        "4-9",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Partial shade to full shade",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Summer",
            "Description": "Purple funnel-shaped flowers, hairy stems and leaves, 1-3 feet tall",
            "Interesting fact": "Each flower opens for only one day but plants bloom continuously all summer"
        }
    ),
    
    "Spiderwort": WildFlower(
        "Spiderwort",
        "Tradescantia ohiensis",
        "Northeast, Southeast",
        "4-9",
        "Non-toxic (edible)",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "14-28",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Partial shade to full sun",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to early summer",
            "Description": "Three-petaled blue-purple flowers, grass-like leaves, 1-3 feet tall",
            "Interesting fact": "Flowers close by noon and young shoots are edible when cooked"
        }
    ),
    
    "Firebush": WildFlower(
        "Firebush",
        "Hamelia patens",
        "Southeast",
        "8-11",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-30",
            "Days to maturity": "120-180"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Low (tender perennial)",
            "Growing season": "Year-round in warm climates",
            "Description": "Orange-red tubular flowers, red stems, 3-8 feet tall",
            "Interesting fact": "Continuous bloomer that attracts hummingbirds, butterflies, and produces berries for birds"
        }
    ),
    
    # Midwest Wildflowers (new additions only - overlapping species already updated above)
    "Prairie Dropseed": WildFlower(
        "Prairie Dropseed",
        "Sporobolus heterolepis",
        "Midwest",
        "3-9",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-30",
            "Days to maturity": "730+ (establishes slowly)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Late summer (flowers), year-round foliage",
            "Description": "Fine-textured grass with airy seed heads, forms clumps 2-3 feet tall",
            "Interesting fact": "Smells like buttered popcorn when blooming and is a keystone prairie species"
        }
    ),
    
    "Wild Indigo": WildFlower(
        "Wild Indigo",
        "Amorpha canescens",
        "Midwest",
        "2-7",
        "Non-toxic",
        {
            "Requires light for germination?": "No (scarification needed)",
            "Days to germinate": "21-30",
            "Days to maturity": "1095+ (3+ years to mature)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Mid to late summer",
            "Description": "Purple flower spikes, silvery compound leaves, 2-4 feet tall",
            "Interesting fact": "Taproot can extend 15 feet deep, making it extremely drought tolerant"
        }
    ),
    
    "Compass Plant": WildFlower(
        "Compass Plant",
        "Silphium laciniatum",
        "Midwest",
        "3-8",
        "Non-toxic",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "14-30",
            "Days to maturity": "1095+ (3-4 years to bloom)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Mid to late summer",
            "Description": "Yellow daisy-like flowers, deeply cut leaves, 6-10 feet tall",
            "Interesting fact": "Leaves orient north-south like a compass, giving it its name"
        }
    ),
    
    "Wild Quinine": WildFlower(
        "Wild Quinine",
        "Parthenium integrifolium",
        "Midwest",
        "3-8",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "7-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Mid to late summer",
            "Description": "Small white composite flowers in flat-topped clusters, 2-5 feet tall",
            "Interesting fact": "Historically used medicinally and attracts over 40 species of beneficial insects"
        }
    ),
    
    "Prairie Phlox": WildFlower(
        "Prairie Phlox",
        "Phlox pilosa",
        "Midwest",
        "4-8",
        "Non-toxic",
        {
            "Requires light for germination?": "No (cold stratification helpful)",
            "Days to germinate": "14-30",
            "Days to maturity": "365+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to early summer",
            "Description": "Pink to purple five-petaled flowers, narrow leaves, 1-2 feet tall",
            "Interesting fact": "One of the earliest prairie flowers to bloom and attracts butterflies and hummingbirds"
        }
    ),
    
    "Rough Blazing Star": WildFlower(
        "Rough Blazing Star",
        "Liatris aspera",
        "Midwest",
        "3-8",
        "Non-toxic",
        {
            "Requires light for germination?": "No (cold stratification helpful)",
            "Days to germinate": "21-30",
            "Days to maturity": "730+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Late summer to early fall",
            "Description": "Purple button-like flowers in tall spikes, 2-5 feet tall",
            "Interesting fact": "Different from meadow blazing star with more widely spaced flower heads"
        }
    ),
    
    "Wild Senna": WildFlower(
        "Wild Senna",
        "Senna hebecarpa",
        "Midwest",
        "4-7",
        "Mildly toxic (medicinal)",
        {
            "Requires light for germination?": "No (scarification needed)",
            "Days to germinate": "14-21",
            "Days to maturity": "120-150"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Mid to late summer",
            "Description": "Yellow flowers with prominent stamens, compound leaves, 3-6 feet tall",
            "Interesting fact": "Host plant for several butterfly species including cloudless sulfur"
        }
    ),
    
    "Nodding Onion": WildFlower(
        "Nodding Onion",
        "Allium cernuum",
        "Midwest",
        "3-9",
        "Non-toxic (edible)",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "21-30",
            "Days to maturity": "730+ (slow from seed)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Late summer",
            "Description": "Pink to white flowers in drooping clusters, grass-like leaves, 1-2 feet tall",
            "Interesting fact": "Attracts beneficial insects and all parts are edible with mild onion flavor"
        }
    ),
    
    # Northwest Wildflowers
    "Camas": WildFlower(
        "Camas",
        "Camassia quamash",
        "Northwest",
        "4-8",
        "Non-toxic (edible bulbs)",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "30-60",
            "Days to maturity": "1460+ (4+ years to bloom from seed)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Low (prefers wet springs)",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to early summer",
            "Description": "Blue to purple star-shaped flowers in tall spikes, 1-4 feet tall",
            "Interesting fact": "Bulbs were a staple food for Native Americans and Lewis & Clark expedition"
        }
    ),
    
    "Pacific Lupine": WildFlower(
        "Pacific Lupine",
        "Lupinus polyphyllus",
        "Northwest",
        "4-8",
        "Toxic (contains alkaloids)",
        {
            "Requires light for germination?": "No (scarification needed)",
            "Days to germinate": "14-30",
            "Days to maturity": "365+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to midsummer",
            "Description": "Tall spikes of blue, purple, or white flowers, 3-5 feet tall",
            "Interesting fact": "Parent of garden lupines and fixes nitrogen in soil"
        }
    ),
    
    "Western Columbine": WildFlower(
        "Western Columbine",
        "Aquilegia formosa",
        "Northwest",
        "5-9",
        "Mildly toxic",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "21-30",
            "Days to maturity": "365+ (blooms second year)"
        },
        {
            "Required sunlight": "Partial shade to full shade",
            "Drought tolerant": "No",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to midsummer",
            "Description": "Red and yellow flowers with long spurs, 2-3 feet tall",
            "Interesting fact": "Specifically evolved for hummingbird pollination with extra-long spurs"
        }
    ),
    
    "Oregon Grape": WildFlower(
        "Oregon Grape",
        "Mahonia aquifolium",
        "Northwest",
        "5-9",
        "Non-toxic (edible berries)",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "30-90",
            "Days to maturity": "1095+ (woody shrub)"
        },
        {
            "Required sunlight": "Partial shade to full shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Early spring flowers, fall berries",
            "Description": "Yellow flower clusters, holly-like leaves, blue berries, 3-6 feet tall",
            "Interesting fact": "Oregon's state flower and important wildlife food source"
        }
    ),
    
    "Fireweed": WildFlower(
        "Fireweed",
        "Chamaenerion angustifolium",
        "Northwest",
        "2-7",
        "Non-toxic (edible)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "7-14",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Moderate",
            "Frost tolerant": "Yes",
            "Growing season": "Summer",
            "Description": "Tall spikes of magenta-pink flowers, 3-8 feet tall",
            "Interesting fact": "First plant to colonize after forest fires, spreads rapidly via wind-dispersed seeds"
        }
    ),
    
    "Western Trillium": WildFlower(
        "Western Trillium",
        "Trillium ovatum",
        "Northwest",
        "5-9",
        "Non-toxic",
        {
            "Requires light for germination?": "No",
            "Days to germinate": "Variable (up to 18 months)",
            "Days to maturity": "2555+ (7+ years to bloom)"
        },
        {
            "Required sunlight": "Full shade to partial shade",
            "Drought tolerant": "No",
            "Frost tolerant": "Yes",
            "Growing season": "Early spring",
            "Description": "Three white petals that fade to pink, three broad leaves, 6-16 inches tall",
            "Interesting fact": "Takes 7+ years to bloom from seed and picking damages the plant permanently"
        }
    ),
    
    "Salmonberry": WildFlower(
        "Salmonberry",
        "Rubus spectabilis",
        "Northwest",
        "6-9",
        "Non-toxic (edible berries)",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "30-60",
            "Days to maturity": "730+ (woody shrub)"
        },
        {
            "Required sunlight": "Partial shade to full shade",
            "Drought tolerant": "No",
            "Frost tolerant": "Yes",
            "Growing season": "Early spring flowers, summer berries",
            "Description": "Pink to red flowers, thorny canes, orange-red berries, 3-12 feet tall",
            "Interesting fact": "Important food source for bears and indigenous peoples of the Pacific Northwest"
        }
    ),
    
    "Western Pasque Flower": WildFlower(
        "Western Pasque Flower",
        "Pulsatilla occidentalis",
        "Northwest",
        "4-7",
        "Toxic (causes skin irritation)",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "30-60",
            "Days to maturity": "730+ (blooms second year)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Early spring (often through snow)",
            "Description": "White to purple cup-shaped flowers, feathery seed heads, 6-16 inches tall",
            "Interesting fact": "One of the first flowers to bloom, often emerging through snow"
        }
    ),
    
    "Red Flowering Currant": WildFlower(
        "Red Flowering Currant",
        "Ribes sanguineum",
        "Northwest",
        "6-9",
        "Non-toxic (edible berries)",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "30-90",
            "Days to maturity": "730+ (woody shrub)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Early spring flowers, summer berries",
            "Description": "Drooping clusters of pink to red flowers, 4-10 feet tall",
            "Interesting fact": "Primary nectar source for rufous hummingbirds during spring migration"
        }
    ),
    
    "Blue Camas": WildFlower(
        "Blue Camas",
        "Camassia leichtlinii",
        "Northwest",
        "4-9",
        "Non-toxic (edible bulbs)",
        {
            "Requires light for germination?": "No (cold stratification needed)",
            "Days to germinate": "30-60",
            "Days to maturity": "1460+ (4+ years to bloom)"
        },
        {
            "Required sunlight": "Full sun to partial shade",
            "Drought tolerant": "Low (prefers wet springs)",
            "Frost tolerant": "Yes",
            "Growing season": "Late spring to early summer",
            "Description": "Tall spikes of blue-purple star flowers, 2-5 feet tall",
            "Interesting fact": "Larger cousin of common camas, creates spectacular meadow displays"
        }
    ),
    
    # Southwest Wildflowers
    "Desert Marigold": WildFlower(
        "Desert Marigold",
        "Baileya multiradiata",
        "Southwest",
        "7-10",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "7-14",
            "Days to maturity": "60-90"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "No",
            "Growing season": "Year-round in warm areas",
            "Description": "Bright yellow daisy-like flowers, silvery-green leaves, 1-3 feet tall",
            "Interesting fact": "Blooms almost continuously and can survive on as little as 3 inches of rain per year"
        }
    ),
    
    "Ghost Plant": WildFlower(
        "Ghost Plant",
        "Monotropa uniflora",
        "Southwest",
        "4-8",
        "Non-toxic",
        {
            "Requires light for germination?": "No (parasitic, no photosynthesis)",
            "Days to germinate": "Variable (depends on host fungi)",
            "Days to maturity": "365+ (complex lifecycle)"
        },
        {
            "Required sunlight": "Full shade (no chlorophyll)",
            "Drought tolerant": "No",
            "Frost tolerant": "Moderate",
            "Growing season": "Summer to early fall",
            "Description": "Pure white translucent stems and flowers, 4-8 inches tall",
            "Interesting fact": "Completely lacks chlorophyll and gets nutrients from fungi in forest soil"
        }
    ),
    
    "Desert Lupine": WildFlower(
        "Desert Lupine",
        "Lupinus sparsiflorus",
        "Southwest",
        "8-10",
        "Toxic (contains alkaloids)",
        {
            "Requires light for germination?": "No (scarification needed)",
            "Days to germinate": "14-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "No",
            "Growing season": "Spring (after winter rains)",
            "Description": "Blue-purple flower spikes, silvery leaves, 1-4 feet tall",
            "Interesting fact": "Only host plant for endangered El Segundo blue butterfly"
        }
    ),
    
    "Desert Willow": WildFlower(
        "Desert Willow",
        "Chilopsis linearis",
        "Southwest",
        "7-9",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-30",
            "Days to maturity": "730+ (woody shrub/tree)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Moderate",
            "Growing season": "Spring through fall",
            "Description": "Orchid-like pink to purple flowers, narrow leaves, 15-25 feet tall",
            "Interesting fact": "Not actually a willow but produces fragrant flowers that attract hummingbirds"
        }
    ),
    
    "Prickly Pear Cactus": WildFlower(
        "Prickly Pear Cactus",
        "Opuntia engelmannii",
        "Southwest",
        "8-11",
        "Non-toxic (edible pads and fruits)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-30",
            "Days to maturity": "1095+ (3+ years to flower)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Moderate",
            "Growing season": "Spring flowers, summer fruits",
            "Description": "Yellow to red flowers, flat paddle-shaped stems, 2-5 feet tall",
            "Interesting fact": "Provides food, water, and shelter for over 60 desert animal species"
        }
    ),
    
    "Desert Paintbrush": WildFlower(
        "Desert Paintbrush",
        "Castilleja chromosa",
        "Southwest",
        "4-8",
        "Mildly toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "21-30",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Spring to early summer",
            "Description": "Bright red-orange bracts, inconspicuous flowers, 1-3 feet tall",
            "Interesting fact": "Semi-parasitic plant that taps into roots of nearby plants for nutrients"
        }
    ),
    
    "Blanket Flower": WildFlower(
        "Blanket Flower",
        "Gaillardia pulchella",
        "Southwest, Midwest",
        "3-10",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "7-21",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Moderate",
            "Growing season": "Spring through fall",
            "Description": "Red and yellow daisy-like flowers, 1-3 feet tall",
            "Interesting fact": "Named for resembling Native American blanket patterns"
        }
    ),
    
    "Ghost Flower": WildFlower(
        "Ghost Flower",
        "Mohavea confertiflora",
        "Southwest",
        "9-11",
        "Non-toxic",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-21",
            "Days to maturity": "60-90"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "No",
            "Growing season": "Spring (after winter rains)",
            "Description": "Translucent white flowers with purple spots, 1-4 feet tall",
            "Interesting fact": "Mimics bee flowers to attract pollinators but provides no nectar reward"
        }
    ),
    
    "Desert Sage": WildFlower(
        "Desert Sage",
        "Artemisia tridentata",
        "Southwest",
        "4-8",
        "Non-toxic (aromatic/medicinal)",
        {
            "Requires light for germination?": "Yes",
            "Days to germinate": "14-30",
            "Days to maturity": "730+ (woody shrub)"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "Yes",
            "Growing season": "Late summer (inconspicuous flowers)",
            "Description": "Silvery-gray aromatic leaves, tiny yellow flowers, 3-8 feet tall",
            "Interesting fact": "Keystone species providing habitat for over 350 animal species including sage grouse"
        }
    ),
    
    "Desert Mallow": WildFlower(
        "Desert Mallow",
        "Sphaeralcea ambigua",
        "Southwest",
        "8-10",
        "Non-toxic",
        {
            "Requires light for germination?": "No (scarification helpful)",
            "Days to germinate": "14-30",
            "Days to maturity": "90-120"
        },
        {
            "Required sunlight": "Full sun",
            "Drought tolerant": "Yes",
            "Frost tolerant": "No",
            "Growing season": "Spring and fall",
            "Description": "Orange cup-shaped flowers, gray-green leaves, 2-4 feet tall",
            "Interesting fact": "Flowers close during hot afternoons to conserve moisture and reopen in evening"
        }
    )
}