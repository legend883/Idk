/* Mode data: ACTION & IMAGINATION shelf. Same format as modes-dream.js. */
(function (T) {
  T.addModes([
    {
      id: 'supervillain', name: 'Dream Supervillain', cat: 'action', kind: 'figure', skin: 'villain',
      blurb: 'Evil powers, a dramatic cape and a ridiculous master plan. Mwahaha.',
      ai: 'a dramatic but family-friendly cartoon supervillain, full body',
      cover: ['🦹', '🌋', '🐍'], color: '#5A189A',
      rounds: [
        ['Evil power', 'aura', [
          'Shadow Control|Command every shadow|🌑|#3C096C',
          'Mind Control|Everyone does your homework|🌀|#9D4EDD',
          'Lightning Hands|Zap anything|⚡|#FFD60A',
          'Goo Powers|Turn into slime|🟢|#70E000']],
        ['Second power', 'aura2', [
          'Shrink Ray Eyes|Shrink things by looking|🔬|#00F5D4',
          'Weather Control|Make it rain on parades|🌩️|#5BC0EB',
          'Clone Army|Make 100 copies of yourself|👥|#F15BB5']],
        ['Costume', 'color', [
          'Dark Purple Cape Suit|Classic villain style|🟪|#4A0E78:cape',
          'Black Armor|Spiky and shiny|⬛|#1B1B1B:cape',
          'Toxic Green Suit|Glows a little|🟩|#38B000:cape',
          'Blood Orange Robe|Flowing and dramatic|🟧|#C2410C:cape']],
        ['Mask or helmet', 'mask', [
          'Horned Helmet|Two giant horns|😈|#2B2D42:helmet',
          'Skull Mask|Spooky but stylish|💀|#E5E5E5:mask',
          'Monocle and Top Hat|Very fancy villain|🎩|#111111:tophat',
          'Robot Face Plate|Red glowing eyes|🤖|#8D99AE:helmet']],
        ['Evil gadget', 'hand', [
          'Freeze Ray|Freezes the city|🧊',
          'Doom Scepter|Glows when evil|🔱',
          'Remote Control of Doom|One big red button|🔴']],
        ['Villain name', 'title', [
          'Doctor Dread|Name|☠️',
          'The Puppet Master|Name|🎭',
          'Lord Mayhem|Name|👹',
          'Countess Chaos|Name|🦇']],
        ['Henchman', 'buddy', [
          'Evil Penguin Army|Waddling minions|🐧',
          'A Grumpy Robot|Hates Mondays|🤖',
          'A Snake Named Steve|Very loyal|🐍']],
        ['Secret lair', 'home', [
          'Volcano Lair|Lava moat included|🌋',
          'Undersea Dome|Shark guards|🦈',
          'Haunted Mansion|Creaky doors|🏚️',
          'Space Station|Orbiting the Moon|🛰️']],
        ['Master plan', 'emblem', [
          'Steal the Moon|Hold it for ransom|🌙',
          'Cancel Summer|Snow in July|☃️',
          'Replace All Pizza with Broccoli|Pure evil|🥦']],
        ['Weakness', 'rival', [
          'Kittens|Too cute to fight|🐈',
          'Bubble Baths|Cannot resist bubbles|🛁',
          'Bad Jokes|Laughs too hard to be evil|😂']]
      ]
    },
    {
      id: 'fantasy-world', name: 'Dream Fantasy World', cat: 'action', kind: 'map', skin: 'fantasy',
      blurb: 'Castles, dragons, magic forests and enchanted creatures. Rule your own realm.',
      ai: 'a magical fantasy kingdom map with castles and dragons',
      cover: ['🐉', '🏰', '🔮'], color: '#2D6A4F',
      rounds: [
        ['Kingdom name', 'banner', [
          'Glimmerdale|Name|✨',
          'Dragonspire|Name|🐉',
          'Mooncrest|Name|🌙',
          'Everbloom|Name|🌸']],
        ['Castle', 'spot', [
          'Crystal Castle|Made of glowing crystal|🏰',
          'Cloud Palace|Floats in the sky|☁️',
          'Treetop Fortress|Built in a giant tree|🌳']],
        ['Magic creature', 'spot', [
          'Friendly Dragon|Gives rides|🐉',
          'Unicorn Herd|Rainbow manes|🦄',
          'Phoenix|Reborn in fire|🐦‍🔥',
          'Griffin|Half eagle, half lion|🦅']],
        ['Enchanted place', 'spot', [
          'Glowing Mushroom Forest|Lights up at night|🍄',
          'Wishing Well|Wishes come true|🪣',
          'Rainbow Waterfall|Every color of water|🌈']],
        ['Wizard', 'spot', [
          'The Grand Wizard|Long beard, big hat|🧙',
          'A Fairy Queen|Tiny but mighty|🧚',
          'A Wise Old Tree|Talks slowly|🌲']],
        ['Mysterious danger', 'spot', [
          'Troll Bridge|Pay the troll a joke|🧌',
          'Dark Forest|Do not go at night|🌲',
          'Sleeping Giant|Shhh|😴']],
        ['Treasure', 'spot', [
          'Dragon Hoard|Mountains of gold|💰',
          'Magic Sword in a Stone|Only you can pull it|🗡️',
          'Crown of Stars|Glows with starlight|👑']],
        ['Village', 'spot', [
          'Hobbit Hills|Round doors in hills|🏡',
          'Elf Village|Bridges in the trees|🧝',
          'Mermaid Lagoon|Underwater town|🧜']],
        ['Transport', 'spot', [
          'Flying Carpet|Smooth ride|🧞',
          'Pegasus Express|Winged horse taxi|🐎',
          'Magic Portal|Go anywhere instantly|🌀']],
        ['Festival', 'spot', [
          'Festival of Lanterns|Thousands in the sky|🏮',
          'Dragon Races|Fastest dragon wins|🏁',
          'Feast of the Realm|Everyone is invited|🍗']]
      ]
    },
    {
      id: 'robot', name: 'Dream Robot', cat: 'action', kind: 'figure', skin: 'robot',
      blurb: 'Chassis, arms, jetpacks and a personality chip. Build your robot buddy.',
      ai: 'a friendly giant robot, full body',
      cover: ['🤖', '🔧', '🚀'], color: '#8D99AE',
      rounds: [
        ['Chassis color', 'color', [
          'Chrome Silver|Shiny like a mirror|🪩|#ADB5BD',
          'Fire Engine Red|Bright and bold|🚒|#D7263D',
          'Gold Plated|Fancy and shiny|🥇|#E8B10C',
          'Space Blue|Deep blue metal|🔵|#1E5AA8']],
        ['Head', 'mask', [
          'TV Screen Face|Shows emoji moods|📺|#222222:screen',
          'Dome Head|Clear dome with gears|🫙|#7FDBFF:dome',
          'Antenna Head|Picks up every channel|📡|#8D99AE:antenna']],
        ['Power core', 'aura', [
          'Fusion Reactor|Glows bright blue|⚛️|#00B4D8',
          'Rainbow Battery|Never runs out|🌈|#F15BB5',
          'Solar Panels|Powered by sunshine|☀️|#FFD60A']],
        ['Arm tool', 'hand', [
          'Laser Pointer|For cats, mostly|🔦',
          'Claw Grabber|Picks up anything|🦾',
          'Pizza Slicer|Very important|🍕',
          'Bubble Blaster|Shoots bubbles|🫧']],
        ['Movement', 'feet', [
          'Rocket Boots|Fly anywhere|🚀',
          'Tank Treads|Rolls over anything|🛞',
          'Spring Legs|Bounces super high|🦘']],
        ['Back attachment', 'back', [
          'Jetpack|Twin flame jets|🔥',
          'Robot Wings|Fold out to fly|🪽',
          'Backpack Snack Bar|Snacks on demand|🍫']],
        ['Robot name', 'title', [
          'Bolt-9000|Name|🔩',
          'Sir Beeps-a-Lot|Name|🔊',
          'Mega Max|Name|🦾',
          'Sparky|Name|⚡']],
        ['Personality chip', 'emblem', [
          'Joke Mode|Tells terrible jokes|😂',
          'Hero Mode|Saves cats from trees|🦸',
          'Chef Mode|Makes perfect pancakes|🥞']],
        ['Robot pet', 'buddy', [
          'Robo Dog|Wags a metal tail|🐕',
          'Drone Bird|Flies on lookout|🐦',
          'Mini Me Bot|A tiny copy of your robot|🤖']],
        ['Home base', 'home', [
          'Garage Workshop|Tools everywhere|🧰',
          'Space Hangar|Launch pad included|🚀',
          'Underwater Dock|Charging station under the sea|⚓']]
      ]
    },
    {
      id: 'animal', name: 'Dream Animal', cat: 'action', kind: 'figure', skin: 'creature',
      blurb: 'Mix wings, horns, colors and powers into a creature nobody has ever seen.',
      ai: 'a cute fantasy hybrid creature, full body',
      cover: ['🦄', '🐉', '🦋'], color: '#FFB703',
      rounds: [
        ['Fur or scales', 'color', [
          'Golden Fur|Soft and shiny|🦁|#F2B134',
          'Rainbow Scales|Shimmers in the sun|🐟|#9B5DE5',
          'Snowy White Fluff|Like a cloud|☁️|#F1F5F9',
          'Leopard Spots|Wild and spotty|🐆|#E09F3E']],
        ['Head feature', 'head', [
          'Unicorn Horn|Sparkly spiral horn|🦄',
          'Bunny Ears|Super long ears|🐰',
          'Antlers|Grand like a stag|🦌',
          'Dragon Horns|Two curved horns|🐲']],
        ['Wings', 'back', [
          'Butterfly Wings|Bright and fluttery|🦋',
          'Dragon Wings|Big leathery wings|🐉',
          'Feathered Wings|Like an eagle|🪶']],
        ['Tail', 'tail', [
          'Fox Tail|Big and bushy|🦊',
          'Mermaid Tail|Swims like a fish|🧜',
          'Peacock Tail|Opens like a fan|🦚']],
        ['Feet', 'feet', [
          'Duck Feet|Webbed and waddly|🦆',
          'Lion Paws|Big soft paws|🐾',
          'Hooves|Click clack|🐴']],
        ['Special power', 'aura', [
          'Glows in the Dark|Like a nightlight|✨|#FFD60A',
          'Breathes Bubbles|Instead of fire|🫧|#7FDBFF',
          'Super Bounce|Bounces like a ball|🏀|#F7931E',
          'Color Change|Like a chameleon|🦎|#70E000']],
        ['Sound it makes', 'emblem', [
          'Purr-Roar|A purr and a roar|🐯',
          'Tiny Hiccups|Very cute|😮',
          'Opera Singing|Sings beautifully|🎶']],
        ['Name', 'title', [
          'Fluffernutter|Name|🥜',
          'Sir Sparkles|Name|✨',
          'Zigzag|Name|〰️',
          'Professor Snuggles|Name|🎓']],
        ['Habitat', 'home', [
          'Rainbow Forest|Trees of every color|🌈',
          'Cloud Kingdom|Lives on clouds|☁️',
          'Volcano Island|Warm and toasty|🌋',
          'Coral Reef|Under the sea|🪸']],
        ['Best friend', 'buddy', [
          'A Tiny Owl|Rides on its head|🦉',
          'A Turtle|Slow but wise|🐢',
          'A Hummingbird|Always buzzing around|🐦']]
      ]
    },
    {
      id: 'island', name: 'Dream Island', cat: 'action', kind: 'map', skin: 'island',
      blurb: 'Your own private island. Fill it with mansions, waterslides and treasure.',
      ai: 'a private tropical island seen from above',
      cover: ['🏝️', '🌴', '🐢'], color: '#00B8A9',
      rounds: [
        ['Island name', 'banner', [
          'Coconut Cove|Name|🥥',
          'Paradise Point|Name|🌅',
          'Treasure Key|Name|🗝️',
          'Turtle Bay|Name|🐢']],
        ['Main house', 'spot', [
          'Beach Mansion|Steps from the sand|🏖️',
          'Giant Treehouse|In the tallest palm|🌴',
          'Glass Dome House|360-degree ocean view|🔮']],
        ['Beach', 'spot', [
          'Pink Sand Beach|Soft pink sand|🩷',
          'Glowing Bay|Water glows at night|✨',
          'Surf Break|Perfect waves daily|🏄']],
        ['Water fun', 'spot', [
          'Water Slide off a Cliff|Into the lagoon|🛝',
          'Jet Ski Dock|Five jet skis|🚤',
          'Floating Trampoline|Bounce into the sea|🤸']],
        ['Wildlife', 'spot', [
          'Sea Turtle Nest|Baby turtles|🐢',
          'Parrot Jungle|Talking parrots|🦜',
          'Friendly Dolphins|Visit every morning|🐬']],
        ['Adventure spot', 'spot', [
          'Secret Cave|Hidden behind a waterfall|🕳️',
          'Volcano Lookout|Steamy and safe|🌋',
          'Shipwreck|Explore the old ship|⚓']],
        ['Food', 'spot', [
          'Coconut Stand|Fresh coconuts|🥥',
          'Beach BBQ Pit|Grill every night|🍖',
          'Tropical Fruit Grove|Mangoes and pineapples|🥭']],
        ['Fun building', 'spot', [
          'Tiki Arcade|Games by the beach|🕹️',
          'Outdoor Cinema|Movies under stars|🎬',
          'Lighthouse|Climb to the top|🗼']],
        ['Treasure', 'spot', [
          'Buried Pirate Chest|X marks the spot|🏴‍☠️',
          'Golden Statue|Mysterious and shiny|🗿',
          'Pearl Lagoon|Pearls everywhere|🦪']],
        ['Getting there', 'spot', [
          'Seaplane|Lands on the water|🛩️',
          'Yacht|Fancy boat|🛥️',
          'Submarine|Arrive underwater|🌊']]
      ]
    },
    {
      id: 'zombie-team', name: 'Dream Zombie Apocalypse Team', cat: 'action', kind: 'team', skin: 'zombie',
      blurb: 'The zombies are coming (slowly). Draft the crew that survives in style.',
      ai: 'a funny cartoon zombie apocalypse survival team, not scary',
      cover: ['🧟', '🔦', '🛡️'], color: '#4F772D',
      rounds: [
        ['Team leader', 'member', [
          'A Retired Ninja|Silent and fast|🥷',
          'A Fearless Grandma|Has seen worse|👵',
          'A Park Ranger|Knows every trail|🧢']],
        ['Muscle', 'member', [
          'A Bodybuilder|Lifts cars|💪',
          'A Lumberjack|Big axe, big heart|🪓',
          'A Sumo Wrestler|Unmovable|🤼']],
        ['Brains', 'member', [
          'A Scientist|Working on a cure|🧪',
          'A Kid Genius|Builds gadgets from junk|🧒',
          'A Librarian|Knows every fact|📚']],
        ['Medic', 'member', [
          'An ER Doctor|Calm under pressure|🩺',
          'A Veterinarian|Also fixes the dog|🐾',
          'A School Nurse|Band-aids for everything|🩹']],
        ['Pet', 'member', [
          'A Guard Dog|Barks at zombies|🐕',
          'A Hawk|Scouts from the sky|🦅',
          'A Very Brave Cat|Hisses at everything|🐈']],
        ['Vehicle', 'gear', [
          'Armored School Bus|Fits everyone|🚌',
          'Monster Truck|Drives over zombies|🛻',
          'Ice Cream Truck|Plays music, distracts zombies|🍦']],
        ['Weapon', 'gear', [
          'Frying Pan|Classic and effective|🍳',
          'Foam Dart Blaster|Zombies hate it|🔫',
          'Giant Water Balloon Launcher|Splash!|🎈']],
        ['Hideout', 'home', [
          'Shopping Mall|Snacks forever|🏬',
          'Castle|Big walls|🏰',
          'Treehouse Fort|Zombies cannot climb|🌳']],
        ['Supplies', 'gear', [
          'Endless Canned Food|Beans for days|🥫',
          'Walkie-Talkies|Stay in touch|📻',
          'Solar Generator|Lights stay on|🔋']],
        ['Secret weapon', 'gear', [
          'Zombie Cure Potion|One sip, back to normal|🧴',
          'Dance Music Speaker|Zombies cannot resist dancing|🔊',
          'Garlic Bread Cannon|They love it more than brains|🥖']]
      ]
    },
    {
      id: 'school', name: 'Dream School', cat: 'action', kind: 'building', skin: 'school',
      blurb: 'Slides between floors, a pizza cafeteria and recess all day. Build the best school.',
      ai: 'a fun dream school building, cutaway view',
      cover: ['🏫', '📚', '🍎'], color: '#FFB703',
      rounds: [
        ['School name', 'sign', [
          'Awesome Academy|Name|🎓',
          'Rocket Ridge School|Name|🚀',
          'Wonder Valley Prep|Name|🌈',
          'Thunderbolt High|Name|⚡']],
        ['Classroom', 'room', [
          'Beanbag Classroom|No desks, just beanbags|🛋️',
          'Treehouse Classroom|Class in the trees|🌳',
          'Space Classroom|Zero gravity lessons|🚀']],
        ['Cafeteria', 'room', [
          'Pizza Every Day|Unlimited slices|🍕',
          'Taco Bar|Build your own|🌮',
          'Dessert First Cafe|Dessert comes first|🍰']],
        ['Recess', 'room', [
          'Mega Playground|Five-story jungle gym|🛝',
          'Zipline Course|Zip across the field|🪂',
          'Water Park Recess|Slides and splash zones|💦']],
        ['Gym', 'room', [
          'Trampoline Gym|Dodgeball on trampolines|🤸',
          'Rock Climbing Wall|Climb to the roof|🧗',
          'Ice Rink|Skate in gym class|⛸️']],
        ['Library', 'room', [
          'Secret Library|Hidden behind a bookshelf|📚',
          'Comic Book Library|Every comic ever|📖',
          'Library with a Slide|Slide down to reading|🛝']],
        ['Special class', 'room', [
          'Video Game Design|Make your own games|🎮',
          'Dragon Training|Very advanced|🐉',
          'Chocolate Making|Delicious homework|🍫']],
        ['Getting to school', 'room', [
          'Rocket Bus|Arrive in 30 seconds|🚀',
          'Zipline from Home|Zip right to class|🪢',
          'Hot Air Balloon|Float to school|🎈']],
        ['School pet', 'room', [
          'A Llama|Very calm|🦙',
          'A Baby Dinosaur|Somehow|🦕',
          'A Talking Parrot|Answers questions|🦜']],
        ['Best rule', 'room', [
          'No Homework Ever|Ever|🚫',
          'Pajama Fridays|Every Friday|🩳',
          'Four-Day Weeks|Three-day weekends|📅']]
      ]
    },
    {
      id: 'secret-hq', name: 'Dream Secret Headquarters', cat: 'action', kind: 'building', skin: 'hq',
      blurb: 'Hidden entrances, gadget labs and a giant mission screen. Top secret.',
      ai: 'a secret underground spy headquarters, cutaway view',
      cover: ['🕵️', '🗝️', '🛰️'], color: '#1B263B',
      rounds: [
        ['Code name', 'sign', [
          'Base Omega|Name|Ω',
          'The Nest|Name|🪺',
          'Project Shadow|Name|🌑',
          'Fort Kaboom|Name|💥']],
        ['Location', 'room', [
          'Under a Mountain|Inside the rock|⛰️',
          'Under the Ocean|Deep below the waves|🌊',
          'Inside a Volcano|Toasty|🌋',
          'In the Clouds|Floating sky base|☁️']],
        ['Secret entrance', 'room', [
          'Phone Booth Elevator|Dial the code|📞',
          'Trash Can Slide|Gross but genius|🗑️',
          'Hollow Tree Door|Knock three times|🌳']],
        ['Mission control', 'room', [
          'Giant Map Screen|Shows the whole world|🗺️',
          'Hologram Table|3D mission plans|🔷',
          'Spy Satellite Link|Sees everything|🛰️']],
        ['Gadget lab', 'room', [
          'Invisibility Cloak Lab|Work in progress|🧥',
          'Jetpack Testing Room|Ceiling is very high|🚀',
          'Shrink Ray Lab|Do not touch|🔬']],
        ['Vehicle bay', 'room', [
          'Spy Car Garage|Turns into a boat|🚗',
          'Mini Submarine Dock|Two-seater sub|🚤',
          'Stealth Jet Hangar|Silent and fast|✈️']],
        ['Training room', 'room', [
          'Laser Maze|Dodge the lasers|🔴',
          'Ninja Dojo|Practice moves|🥋',
          'Obstacle Course|Timed runs|⏱️']],
        ['Living quarters', 'room', [
          'Bunk Pods|Sleeping capsules|🛏️',
          'Game Lounge|Relax between missions|🎮',
          'Snack Vault|Highly guarded snacks|🍫']],
        ['Security', 'room', [
          'Robot Guards|Never sleep|🤖',
          'Retina Scanner|Only your eye opens it|👁️',
          'Guard Dogs|Very good dogs|🐕']],
        ['Escape route', 'room', [
          'Rocket Escape Pod|Blast off|🚀',
          'Underground Train|Secret tunnel ride|🚇',
          'Zipline to the Ocean|Splash landing|🪂']]
      ]
    },
    {
      id: 'adventure-team', name: 'Dream Adventure Team', cat: 'action', kind: 'team', skin: 'adventure',
      blurb: 'Explorers, guides and gear for the lost temple. Assemble the expedition.',
      ai: 'an adventure expedition team in front of a jungle temple',
      cover: ['🧭', '🗺️', '🏺'], color: '#BC6C25',
      rounds: [
        ['Mission', 'banner', [
          'Find the Lost Temple|Deep in the jungle|🛕',
          'Climb the Tallest Mountain|Above the clouds|🏔️',
          'Explore the Deep Sea|Darkest trench|🌊',
          'Map a Hidden Cave|Nobody has ever been inside|🦇']],
        ['Leader', 'member', [
          'A Famous Explorer|Has a cool hat|🤠',
          'A Mountain Guide|Knows every path|🧗',
          'A Ship Captain|Steers through storms|⚓']],
        ['Expert', 'member', [
          'An Archaeologist|Reads ancient writing|🏺',
          'A Map Maker|Never gets lost|🗺️',
          'A Codebreaker|Solves every puzzle|🔐']],
        ['Strong one', 'member', [
          'A Rock Climber|Climbs anything|🧗',
          'A Strongman|Moves boulders|🪨',
          'A Swimmer|Holds breath for ten minutes|🏊']],
        ['Funny one', 'member', [
          'A Comedian|Keeps spirits up|🎭',
          'A Clumsy Assistant|Trips into discoveries|🤪',
          'A Parrot That Talks Too Much|Squawk|🦜']],
        ['Animal partner', 'member', [
          'A Trusty Horse|Fast and loyal|🐎',
          'A Camel|Desert expert|🐫',
          'A Brave Monkey|Swings ahead|🐒']],
        ['Vehicle', 'gear', [
          'Jungle Jeep|Muddy and tough|🚙',
          'Airship|Floats over everything|🎈',
          'Submarine|Goes deep|🚢']],
        ['Gear', 'gear', [
          'Magic Compass|Points to treasure|🧭',
          'Rope and Grappling Hook|Climb anything|🪝',
          'Night Vision Goggles|See in the dark|🥽']],
        ['Snack supply', 'gear', [
          'Trail Mix Mountain|Endless trail mix|🥜',
          'Campfire S\'mores Kit|Every night|🔥',
          'Pizza Drone Delivery|Even in the jungle|🍕']],
        ['Prize', 'gear', [
          'Golden Idol|Very shiny|🗿',
          'Dragon Egg|Warm to touch|🥚',
          'Ancient Map|Leads to more adventure|📜']]
      ]
    },
    {
      id: 'superpower-team', name: 'Dream Superpower Team', cat: 'action', kind: 'team', skin: 'powers',
      blurb: 'Draft a squad of heroes whose powers combine into something unstoppable.',
      ai: 'a superhero team lineup, comic book style',
      cover: ['⚡', '🦸', '🔥'], color: '#0077FF',
      rounds: [
        ['Team name', 'title', [
          'The Mighty Five|Name|✋',
          'Team Thunder|Name|⚡',
          'The Galaxy Guard|Name|🌌',
          'The Unstoppables|Name|💥']],
        ['Leader power', 'member', [
          'Flight|Leads from the sky|🕊️',
          'Super Strength|Lifts the team|💪',
          'Lightning|Charges ahead|⚡']],
        ['Speedster', 'member', [
          'Super Speed|Faster than light|💨',
          'Teleporter|Blinks across town|✨',
          'Time Stopper|Freezes the clock|⏱️']],
        ['Elemental', 'member', [
          'Fire Master|Hot stuff|🔥',
          'Ice Master|Cool head|❄️',
          'Water Bender|Rides on waves|🌊',
          'Plant Grower|Vines everywhere|🌿']],
        ['Mind power', 'member', [
          'Telepath|Reads minds|🧠',
          'Telekinetic|Moves things with thought|🌀',
          'Future Seer|Knows what is next|🔮']],
        ['Defender', 'member', [
          'Force Field|Bubble shield|🛡️',
          'Rock Skin|Unbreakable|🪨',
          'Healer|Fixes everyone|💚']],
        ['Wildcard', 'member', [
          'Shrinker|Ant-sized hero|🐜',
          'Stretchy|Bends like rubber|🤸',
          'Animal Shifter|Turns into any animal|🐺']],
        ['Team vehicle', 'gear', [
          'Hero Jet|Supersonic|✈️',
          'Mega Mech|Combines into a giant robot|🤖',
          'Star Cruiser|Space travel|🚀']],
        ['Headquarters', 'home', [
          'Sky Fortress|Floating base|🏰',
          'Moon Tower|On the Moon|🌕',
          'Underground Bunker|Secret lair|🕳️']],
        ['Team gadget', 'gear', [
          'Hero Watches|Call the team|⌚',
          'Combo Power Crystal|Combines powers|💎',
          'Hero Signal|Light in the sky|🔦']]
      ]
    }
  ]);
})(window.TDA);
