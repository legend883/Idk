/* Mode data: BUILD YOUR DREAM shelf.
   Item string format: "Name|Short description|emoji|extra"
   extra is optional: a color (#hex) and/or a shape (e.g. "#d22:helmet").
   Round format: [label, part, [items...]]; part tells the renderer where the item lands. */
(function (T) {
  T.addModes([
    {
      id: 'house', name: 'Dream House', cat: 'dream', kind: 'building', skin: 'house',
      blurb: 'Pools, theaters, secret rooms. Build the house everyone wants to sleep over at.',
      ai: 'a cutaway dream house with every room visible',
      cover: ['🏠', '🏊', '🎬'], color: '#00A6E8',
      rounds: [
        ['Outdoor splash', 'room', [
          'Swimming Pool|Crystal-blue pool with a diving board|🏊',
          'Moon Pool|A glowing pool that opens to the ocean below|🌊',
          'Hot Tub|Bubbling hot tub under the stars|♨️',
          'Lazy River|A slow river that loops around the yard|🛟']],
        ['Get moving', 'room', [
          'Private Gym|Weights, treadmills and a smoothie bar|🏋️',
          'Basketball Court|Full court with your name at center|🏀',
          'Tennis Court|Clay court with stadium lights|🎾',
          'Trampoline Room|Wall-to-wall trampolines and foam pit|🤸']],
        ['Showtime', 'room', [
          'Movie Theater|Reclining seats and a popcorn machine|🎬',
          'Music Room|Drums, guitars and a recording booth|🎸',
          'Karaoke Lounge|Disco ball and a song list of 10,000 hits|🎤']],
        ['Play zone', 'room', [
          'Gaming Room|Every console, giant screen, beanbags|🎮',
          'Arcade|Classic cabinets with free play forever|🕹️',
          'Bowling Alley|Two lanes and glow-in-the-dark pins|🎳',
          'Golf Simulator|Play famous courses from the couch|⛳']],
        ['Chill out', 'room', [
          'Sauna|Cedar sauna that smells like a forest|🧖',
          'Giant Aquarium|A wall of fish and a friendly shark|🐠',
          'Indoor Swimming Pool|Swim all winter under a glass roof|🏊‍♂️']],
        ['Up top', 'room', [
          'Rooftop Terrace|Hammocks, string lights and a city view|🌇',
          'Observatory Dome|Your own telescope for the night sky|🔭',
          'Helipad|Land the family chopper on the roof|🚁']],
        ['Style & stuff', 'room', [
          'Walk-in Closet|A rotating closet like a movie star|👗',
          'Sneaker Vault|Glass cases for 300 pairs of kicks|👟',
          'Candy Pantry|A pantry stocked like a candy shop|🍬']],
        ['Brain space', 'room', [
          'Home Library|Rolling ladders and a hidden reading nook|📚',
          'Science Lab|Bubbling beakers and safety goggles|🧪',
          'Art Studio|Paint everywhere and nobody minds|🎨']],
        ['Getting around', 'room', [
          'Elevator|Glass elevator to every floor|🛗',
          'Giant Slide|Slide from your bedroom to the kitchen|🛝',
          'Fire Pole|Zoom down to breakfast like a firefighter|🚒']],
        ['Secret feature', 'room', [
          'Secret Passage|A bookshelf that swings open|🗝️',
          'Panic Room Fort|Pillow fort with steel walls|🏰',
          'Underground Garage|Room for a dozen dream cars|🚗',
          'Pet Palace|A mini mansion for the family pets|🐶']]
      ]
    },
    {
      id: 'food-day', name: 'Dream Day of Food', cat: 'dream', kind: 'spread', skin: 'day',
      blurb: 'Breakfast to midnight snack. Bid on the most delicious day ever eaten.',
      ai: 'a full day of food laid out from breakfast to late-night snack',
      cover: ['🥞', '🍔', '🍦'], color: '#F7931E',
      rounds: [
        ['Breakfast', 'meal', [
          'Pancake Tower|Ten fluffy pancakes with syrup waterfall|🥞',
          'Belgian Waffles|Crispy waffles with strawberries and cream|🧇',
          'Bacon & Eggs|Sizzling bacon with sunny-side eggs|🍳',
          'French Toast|Cinnamon French toast with powdered sugar|🍞']],
        ['Morning drink', 'meal', [
          'Fresh OJ|Squeezed this morning, extra pulp optional|🍊',
          'Hot Chocolate|With a mountain of marshmallows|☕',
          'Berry Smoothie|Blended strawberries, blueberries and banana|🥤']],
        ['Lunch', 'meal', [
          'Double Cheeseburger|Two patties, melty cheese, special sauce|🍔',
          'Pizza Party|A whole pizza just for you|🍕',
          'Taco Trio|Three tacos loaded with everything|🌮',
          'Sushi Platter|Rainbow rolls and salmon nigiri|🍣']],
        ['Side dish', 'meal', [
          'Curly Fries|Seasoned and extra crispy|🍟',
          'Mac and Cheese|Baked with a golden crunchy top|🧀',
          'Onion Rings|Giant rings, perfect for dipping|🧅']],
        ['Afternoon snack', 'meal', [
          'Soft Pretzel|Warm pretzel with cheese dip|🥨',
          'Popcorn Bucket|Movie-theater butter, bottomless|🍿',
          'Nachos Supreme|Cheese, salsa, guac, the works|🫔']],
        ['Dinner', 'meal', [
          'Spaghetti & Meatballs|Grandma-style giant meatballs|🍝',
          'Fried Chicken|Crispy, juicy, secret-recipe chicken|🍗',
          'Steak Dinner|Perfect steak with mashed potatoes|🥩',
          'Ramen Bowl|Rich broth, noodles and a soft egg|🍜']],
        ['Dessert', 'meal', [
          'Brownie Sundae|Warm brownie under ice cream|🍨',
          'Cookie Jar|A jar of warm chocolate chip cookies|🍪',
          'Birthday Cake|It is not your birthday. Eat it anyway|🎂']],
        ['Sweet treat', 'meal', [
          'Donut Box|A dozen glazed and sprinkled donuts|🍩',
          'Cotton Candy|A cloud of pink sugar|🍭',
          'Churros|Cinnamon sugar churros with chocolate|🥖']],
        ['Drink of the day', 'meal', [
          'Chocolate Milkshake|Thick enough to bend the straw|🥤',
          'Lemonade Stand|Pink lemonade on tap|🍋',
          'Root Beer Float|Fizzy, creamy, perfect|🍺']],
        ['Late-night snack', 'meal', [
          'Midnight Grilled Cheese|Gooey and golden at 12am|🥪',
          'Ice Cream Pint|Eaten straight from the carton|🍦',
          'Cereal Bowl|The good cereal, the sugary one|🥣',
          'Leftover Pizza|Cold pizza, the best kind|🍕']]
      ]
    },
    {
      id: 'superhero', name: 'Dream Superhero', cat: 'dream', kind: 'figure', skin: 'hero',
      blurb: 'Powers, costume, gadgets and a sidekick. Create the hero the world needs.',
      ai: 'a superhero character standing heroically, full body',
      cover: ['🦸', '⚡', '🛡️'], color: '#ED1C24',
      rounds: [
        ['Superpower', 'aura', [
          'Flight|Soar above the clouds at jet speed|🕊️|#5BC0EB',
          'Super Strength|Lift trucks with one hand|💪|#ED1C24',
          'Super Speed|Run faster than sound|⚡|#FFD60A',
          'Invisibility|Vanish whenever you want|👻|#B8B8FF']],
        ['Second power', 'aura2', [
          'Telekinesis|Move things with your mind|🌀|#9B5DE5',
          'Fire Powers|Throw fireballs and fly on flames|🔥|#FF7A00',
          'Ice Powers|Freeze anything solid|❄️|#7FDBFF',
          'Teleportation|Blink anywhere on Earth|✨|#F15BB5']],
        ['Costume', 'color', [
          'Classic Red Suit|Bold red with a flowing cape|🟥|#D7263D:cape',
          'Midnight Armor|Dark blue armored suit|🟦|#1B3A8C:cape',
          'Golden Suit|Shiny gold that sparkles in the sun|🟨|#E8B10C',
          'Emerald Suit|Green suit with lightning trim|🟩|#1E9E55:cape']],
        ['Mask or helmet', 'mask', [
          'Domino Mask|Classic eye mask, identity safe|🎭|#111111:mask',
          'Robo Helmet|Full helmet with a glowing visor|⛑️|#8D99AE:helmet',
          'Star Crown|A crown of starlight|👑|#FFD60A:crown',
          'Hood & Goggles|Mysterious hood with night goggles|🥽|#3A3A3A:hood']],
        ['Gadget', 'hand', [
          'Power Shield|Bounces back anything|🛡️',
          'Grappling Hook|Swing across the city|🪝',
          'Energy Sword|A blade made of light|🗡️',
          'Utility Belt|A gadget for every problem|🧰']],
        ['Hero name', 'title', [
          'Captain Thunder|Name|⚡',
          'The Blur|Name|💨',
          'Nova Knight|Name|🌟',
          'Mega Marvel|Name|🦸']],
        ['Sidekick', 'buddy', [
          'Robo Pup|A robot dog that fetches villains|🐕',
          'Wonder Owl|Wise owl with night vision|🦉',
          'Kid Comet|A super-fast young hero in training|☄️',
          'Shadow Cat|A cat who can walk through walls|🐈‍⬛']],
        ['Headquarters', 'home', [
          'Sky Tower|A tower above the city skyline|🏙️',
          'Volcano Base|Hidden inside a sleeping volcano|🌋',
          'Moon Base|Watch the whole planet from the Moon|🌕',
          'Ice Fortress|A crystal fortress at the North Pole|🏔️']],
        ['Special ability', 'emblem', [
          'X-Ray Vision|See through walls|👁️',
          'Healing Factor|Bounce back from anything|💚',
          'Animal Talk|Talk to every animal|🐾',
          'Time Freeze|Pause time for ten seconds|⏳']],
        ['Arch-nemesis', 'rival', [
          'Dr. Gloom|Wants to make every day a Monday|🌧️',
          'The Glitch|Hacks every screen in the city|👾',
          'Baron Bonkers|Fills the city with clowns|🤡',
          'Queen Frostbite|Wants endless winter|🥶']]
      ]
    },
    {
      id: 'movie', name: 'Dream Movie', cat: 'dream', kind: 'poster', skin: 'movie',
      blurb: 'Cast it, set it, twist it. Make the blockbuster everyone lines up for.',
      ai: 'a blockbuster movie poster',
      cover: ['🎬', '🍿', '⭐'], color: '#9B5DE5',
      rounds: [
        ['Movie genre', 'theme', [
          'Space Adventure|Rockets, aliens and lasers|🚀|#1B1B4B',
          'Spooky Comedy|Ghosts that are mostly funny|👻|#3D2C5E',
          'Jungle Quest|Lost temples and wild animals|🌴|#1F5E3B',
          'Superhero Showdown|Capes, explosions, city in danger|💥|#B3001B']],
        ['Lead star', 'lead', [
          'A Fearless Astronaut|The brave lead who never backs down|👩‍🚀',
          'A Kid Detective|Solves every mystery by bedtime|🕵️',
          'A Talking Dog|Sarcastic, loyal, very good boy|🐕',
          'A Knight in Shining Armor|Honor, sword, terrible jokes|🤺']],
        ['Co-star', 'cast', [
          'A Grumpy Wizard|Powerful but needs a nap|🧙',
          'A Robot Best Friend|Learning what feelings are|🤖',
          'A Pirate Captain|Sails every sea, steals every scene|🏴‍☠️',
          'A Famous Chef|Cooks their way out of danger|👨‍🍳']],
        ['Villain', 'villain', [
          'An Evil Snowman|Wants to freeze summer forever|☃️',
          'A Giant Octopus|Eight arms, zero chill|🐙',
          'A Shadow King|Rules the dark side of the moon|🌑',
          'A Mad Scientist|Too many experiments, not enough rules|🧪']],
        ['Supporting character', 'cast', [
          'A Clumsy Dragon|Sneezes fire at the worst times|🐉',
          'A Wise Grandma|Knows karate and secrets|👵',
          'A Tiny Alien|Only says one word, very loudly|👽',
          'A Unicorn Sidekick|Sparkly, dramatic, fast|🦄']],
        ['Setting', 'setting', [
          'A Floating City|Buildings in the clouds|☁️',
          'An Underwater Kingdom|Coral castles and sea creatures|🐠',
          'A Haunted Mall|Every store is a little cursed|🏬',
          'A Desert Planet|Two suns and endless sand|🏜️']],
        ['Director', 'credit', [
          'The Explosion Expert|Every scene ends with a boom|💣',
          'The Tearjerker|You will cry. Twice|😭',
          'The Comedy Genius|Jokes per minute: off the charts|😂']],
        ['Special skill', 'credit', [
          'Time Travel|Fix the past, break the future|⌛',
          'Shape-Shifting|Become anyone or anything|🦎',
          'Mind Reading|Hear every secret thought|🧠']],
        ['Plot twist', 'tagline', [
          'The Villain Is Their Twin|Nobody saw this coming|👯',
          'It Was All a Video Game|Game over? Or level up?|🎮',
          'The Dog Was the Hero All Along|Good boy saves the world|🐾']],
        ['Ending', 'tagline', [
          'Epic Victory Parade|Confetti over the whole city|🎉',
          'Cliffhanger Sequel|To be continued...|🧗',
          'Big Wedding|Everybody dances|💒',
          'Fly Off Into the Sunset|Credits roll on a sunset|🌅']]
      ]
    },
    {
      id: 'vacation', name: 'Dream Vacation', cat: 'dream', kind: 'map', skin: 'beach',
      blurb: 'Destination, hotel, adventures and room service. Plan the trip of a lifetime.',
      ai: 'a tropical dream vacation destination seen from above',
      cover: ['🏝️', '✈️', '🍹'], color: '#00B8A9',
      rounds: [
        ['Destination', 'spot', [
          'Hawaii|Volcanoes, surf and pineapples|🌺',
          'Tokyo|Neon lights and the best snacks on Earth|🗼',
          'Paris|Croissants under the Eiffel Tower|🥐',
          'Maldives|Huts right on the turquoise water|🏝️']],
        ['Hotel or resort', 'spot', [
          'Overwater Bungalow|Fish swim under your floor|🛖',
          'Castle Hotel|Sleep like royalty|🏰',
          'Treehouse Resort|Rooms high in the rainforest|🌳']],
        ['Transportation', 'spot', [
          'Private Jet|No lines, all snacks|🛩️',
          'Luxury Cruise Ship|A floating city with water slides|🛳️',
          'Hot Air Balloon|Float there slowly and dramatically|🎈']],
        ['Beach or mountain', 'spot', [
          'White Sand Beach|Soft sand and calm waves|🏖️',
          'Snowy Mountain Lodge|Skiing and hot cocoa|🏔️',
          'Jungle Waterfall|Swim under a waterfall|🏞️']],
        ['Adventure', 'spot', [
          'Swim with Dolphins|Friendly dolphins say hi|🐬',
          'Ziplining|Fly over the treetops|🪂',
          'Scuba Diving|Explore a coral reef|🤿',
          'Safari Ride|Lions, giraffes and elephants|🦒']],
        ['Entertainment', 'spot', [
          'Fireworks Show|Every single night|🎆',
          'Concert on the Beach|Your favorite band, front row|🎶',
          'Magic Show|A magician who actually does magic|🎩']],
        ['Restaurant', 'spot', [
          'Underwater Restaurant|Eat dinner with the sharks|🦈',
          'Endless Buffet|Every food, every hour|🍽️',
          'Ice Cream Bar|Unlimited scoops, unlimited toppings|🍨']],
        ['Pool or water park', 'spot', [
          'Infinity Pool|Looks like it pours into the ocean|🌅',
          'Water Park|Twelve slides and a wave pool|💦',
          'Swim-up Snack Bar|Order smoothies without leaving the pool|🍹']],
        ['Room upgrade', 'spot', [
          'Presidential Suite|Bigger than most houses|🛏️',
          'Glass-Floor Room|Stand over the ocean|🪟',
          'Room with a Slide|Slide straight into the pool|🛝']],
        ['Special excursion', 'spot', [
          'Volcano Helicopter Tour|See lava from above|🚁',
          'Private Island Day|Your own island for a day|🏝️',
          'Submarine Ride|Visit a shipwreck|🚢',
          'Northern Lights Trip|Sky turns green and purple|🌌']]
      ]
    },
    {
      id: 'theme-park', name: 'Dream Theme Park', cat: 'dream', kind: 'map', skin: 'park',
      blurb: 'Coasters, mascots, food stands and a night show. Open the best park on Earth.',
      ai: 'a colorful theme park map seen from above',
      cover: ['🎢', '🎡', '🎠'], color: '#E6007E',
      rounds: [
        ['Main theme', 'banner', [
          'Dino World|Dinosaurs around every corner|🦖',
          'Space Kingdom|Rockets, planets and aliens|🪐',
          'Candy Land|Everything looks edible|🍭',
          'Pirate Cove|Ships, treasure and cannons|🏴‍☠️']],
        ['Roller coaster', 'spot', [
          'The Screamer|Ten loops and a 90-degree drop|🎢',
          'Wooden Wildcat|Classic rattling wooden coaster|🐆',
          'Launch Rocket|0 to 100 in two seconds|🚀']],
        ['Water ride', 'spot', [
          'Log Flume|You will get soaked|🪵',
          'River Rapids|Spin down wild rapids|🌊',
          'Splash Mountain Drop|Giant splash at the bottom|💦']],
        ['Thrill ride', 'spot', [
          'Drop Tower|Fall 30 floors in seconds|🗼',
          'Giant Swing|Swing high over the park|🎠',
          'Spinning Teacups|Spin until you are dizzy|☕']],
        ['Family attraction', 'spot', [
          'Ferris Wheel|See the whole park from the top|🎡',
          'Carousel|Ride golden horses and dragons|🎠',
          'Bumper Cars|Crash into your cousins|🚗']],
        ['Food stand', 'spot', [
          'Giant Turkey Legs|Big enough for two|🍗',
          'Funnel Cake Stand|Powdered sugar everywhere|🧁',
          'Cotton Candy Cart|Rainbow flavors|🍭']],
        ['Park mascot', 'spot', [
          'Max the Mouse|Big ears, bigger smile|🐭',
          'Rex the Friendly Dino|Gives the best hugs|🦕',
          'Captain Penguin|Waddles in a pirate hat|🐧']],
        ['Signature attraction', 'spot', [
          'Haunted Castle|Ghosts that chase you|🏰',
          'Volcano Coaster|Ride through lava|🌋',
          'Space Simulator|Feels like real zero gravity|🛸']],
        ['Arcade', 'spot', [
          'Prize Arcade|Win giant stuffed animals|🧸',
          'Laser Tag Arena|Glow-in-the-dark battles|🔫',
          'Retro Game Hall|Hundreds of classic games|🕹️']],
        ['Nighttime show', 'spot', [
          'Fireworks Finale|Fireworks over the castle|🎆',
          'Drone Light Show|500 drones make pictures in the sky|🛰️',
          'Laser Parade|Glowing floats and music|🎇']]
      ]
    },
    {
      id: 'gaming-setup', name: 'Dream Gaming Setup', cat: 'dream', kind: 'stage', skin: 'gaming',
      blurb: 'PC, chair, screens and lights. Build the battle station of your dreams.',
      ai: 'an epic gaming room setup with RGB lights',
      cover: ['🎮', '🖥️', '🎧'], color: '#3A0CA3',
      rounds: [
        ['Room theme', 'wall', [
          'Neon Cyber Room|Pink and blue neon everywhere|🌆|#2B0A5A',
          'Space Station|Stars outside the window|🌌|#0B1A3A',
          'Treehouse Den|Gaming in the treetops|🌲|#1E4D2B',
          'Ice Cave|Cool blue glowing walls|🧊|#0E4C6E']],
        ['Gaming PC', 'pc', [
          'Liquid-Cooled Tower|Glows like a lava lamp|🖥️',
          'Quantum Rig|Runs every game at max|💽',
          'Mini Beast PC|Tiny box, huge power|📦']],
        ['Console', 'console', [
          'Every Console Ever|All of them, stacked up|🎮',
          'Retro Console Wall|Classic consoles on display|🕹️',
          'VR Headset Station|Step into the game|🥽']],
        ['Monitor', 'monitor', [
          'Triple Curved Screens|Wraps all the way around you|🖥️',
          'Wall-Sized TV|Takes up the entire wall|📺',
          'Holographic Display|Games float in the air|🔮']],
        ['Gaming chair', 'chair', [
          'Racing Throne|Built like a race car seat|💺',
          'Massage Chair|Massages you while you play|🪑',
          'Beanbag Mountain|The biggest beanbag ever made|🛋️']],
        ['Keyboard & mouse', 'desk-item', [
          'Rainbow Mechanical Keyboard|Clicky and glowing|⌨️',
          'Pro Gaming Mouse|20 buttons, zero lag|🖱️',
          'Golden Controller|Custom gold controller|🎮']],
        ['Headset', 'desk-item', [
          'Wireless Studio Headset|Hear footsteps a mile away|🎧',
          'Cat-Ear Headset|Glowing cat ears|🐱',
          'Surround Sound Speakers|Shake the whole room|🔊']],
        ['Desk', 'desk', [
          'L-Shaped Battle Desk|Room for everything|🗄️',
          'Floating Glass Desk|Looks like magic|🪟',
          'Stand-Up Desk|Raise and lower with a button|⬆️']],
        ['Lighting', 'light', [
          'RGB Light Strips|16 million colors|🌈|#F15BB5',
          'Lava Lamps|Groovy glowing blobs|🫧|#FF7A00',
          'Starry Ceiling|Twinkling star ceiling|⭐|#5BC0EB']],
        ['Favorite game', 'poster', [
          'Block Builder|Build anything, block by block|🧱',
          'Kart Racers|Banana peels and blue shells|🏎️',
          'Battle Royale|Last one standing wins|🪂',
          'Dungeon Quest|Swords, dragons and loot|🐉']]
      ]
    },
    {
      id: 'car', name: 'Dream Car', cat: 'dream', kind: 'vehicle', skin: 'car',
      blurb: 'Paint, wheels, sound system and gadgets. Build the ride that turns every head.',
      ai: 'a custom dream car, side view, studio lighting',
      cover: ['🏎️', '🔥', '🏁'], color: '#ED1C24',
      rounds: [
        ['Car style', 'body', [
          'Supercar|Low, wide and very fast|🏎️|sport',
          'Monster Truck|Giant tires, crushes everything|🛻|truck',
          'Classic Convertible|Top down, hair blowing|🚘|classic',
          'Futuristic Hover Car|Floats an inch off the road|🛸|hover']],
        ['Paint color', 'paint', [
          'Candy Apple Red|Glossy and bright|🍎|#D7263D',
          'Galaxy Purple|Sparkles like the night sky|🌌|#5A189A',
          'Electric Blue|Bright as a lightning bolt|⚡|#0077FF',
          'Lime Green|Impossible to miss|🍏|#5BCB2B']],
        ['Wheels', 'wheels', [
          'Gold Rims|Shiny gold spinners|🟡|#E8B10C',
          'Glow-in-the-Dark Tires|Light up the road|🟢|#3DFF8B',
          'Flame Rims|Wheels with painted flames|🔥|#FF7A00']],
        ['Interior', 'badge', [
          'Leather Lounge|Seats like a fancy couch|🛋️',
          'Snack Bar|Mini fridge and candy drawer|🍫',
          'Massage Seats|Every seat is a spa|💆']],
        ['Sound system', 'badge', [
          'Thunder Bass|Rattles windows down the street|🔊',
          'Concert Speakers|Sounds like a live show|🎶',
          'Karaoke Mic|Sing along on every drive|🎤']],
        ['Performance', 'badge', [
          'Rocket Booster|Push button, go zoom|🚀',
          'Turbo Engine|Twice the horsepower|⚙️',
          'Jump Springs|Hop over traffic|🦘']],
        ['Lighting', 'glow', [
          'Neon Underglow|Glows under the car|💡|#F15BB5',
          'Laser Headlights|See a mile ahead|🔦|#5BC0EB',
          'Disco Lights|Party on wheels|🪩|#FFD60A']],
        ['Entertainment', 'badge', [
          'Backseat Movie Screens|Every seat gets a screen|📺',
          'Game Console Built In|Play on road trips|🎮',
          'Popcorn Maker|Fresh popcorn on the go|🍿']],
        ['Special tech', 'badge', [
          'Self-Driving Mode|It drives, you nap|🤖',
          'Flying Mode|Wings pop out|🪽',
          'Submarine Mode|Drive under the ocean|🤿']],
        ['Custom design', 'decal', [
          'Racing Stripes|Two bold stripes down the middle|🏁',
          'Flame Decals|Flames down both sides|🔥',
          'Lightning Bolts|Electric bolts on the doors|⚡',
          'Shark Teeth|Teeth painted on the front|🦈']]
      ]
    },
    {
      id: 'bedroom', name: 'Dream Bedroom', cat: 'dream', kind: 'stage', skin: 'bedroom',
      blurb: 'Bunk beds, slides, secret doors. Design the room you never want to leave.',
      ai: 'an amazing kids dream bedroom interior',
      cover: ['🛏️', '🧸', '🌙'], color: '#F15BB5',
      rounds: [
        ['Room theme', 'wall', [
          'Outer Space|Planets painted on the walls|🪐|#1B2A5C',
          'Under the Sea|Waves and fish everywhere|🐳|#0E6E8C',
          'Enchanted Forest|Trees and fairy lights|🍄|#2D6A4F',
          'Candy Land|Pastel candy everything|🍬|#C9184A']],
        ['Bed', 'bed', [
          'Race Car Bed|Vroom to sleep|🏎️',
          'Treehouse Bunk|Ladder up to a treehouse bed|🌳',
          'Cloud Bed|Floats like a cloud|☁️',
          'Pirate Ship Bed|Sail to dreamland|🏴‍☠️']],
        ['Way in or out', 'door', [
          'Secret Bookshelf Door|Pull the right book|📚',
          'Slide to the Kitchen|Snacks in three seconds|🛝',
          'Fire Pole|Zoom downstairs|🚒']],
        ['Screen', 'screen', [
          'Giant TV|Bigger than the bed|📺',
          'Projector Ceiling|Movies on the ceiling|📽️',
          'Gaming Corner|Console and beanbags|🎮']],
        ['Cozy spot', 'nook', [
          'Reading Nook|Pillows and fairy lights|📖',
          'Hammock|Swing while you read|🪢',
          'Ball Pit|Thousands of colorful balls|🔴']],
        ['Pet', 'pet', [
          'A Puppy|Sleeps at the foot of the bed|🐶',
          'A Kitten|Purrs you to sleep|🐱',
          'A Giant Fish Tank|With a tiny shipwreck|🐠',
          'A Bunny|Fluffy and hops around|🐰']],
        ['Lighting', 'light', [
          'Glow-in-the-Dark Stars|A whole galaxy on the ceiling|⭐|#FFD60A',
          'Lava Lamps|Blobby and groovy|🫧|#FF7A00',
          'Color-Changing LEDs|Any color you want|🌈|#9B5DE5']],
        ['Storage', 'shelf', [
          'Toy Wall|Shelves floor to ceiling|🧸',
          'Trophy Case|Show off every award|🏆',
          'Sneaker Wall|Every pair on display|👟']],
        ['Snack station', 'nook', [
          'Mini Fridge|Cold drinks always|🧃',
          'Candy Dispenser|A gumball machine of your own|🍬',
          'Popcorn Machine|For movie nights|🍿']],
        ['Wow feature', 'ceiling', [
          'Climbing Wall|Climb to the ceiling|🧗',
          'Indoor Swing|Swing in your room|🎠',
          'Skylight Telescope|Look at the stars|🔭',
          'Rooftop Hatch|Climb out to a secret deck|🪜']]
      ]
    },
    {
      id: 'restaurant', name: 'Dream Restaurant', cat: 'dream', kind: 'building', skin: 'restaurant',
      blurb: 'Cuisine, signature dish, theme and name. Open the hottest table in town.',
      ai: 'a fun themed restaurant, cutaway view, with its menu',
      cover: ['🍽️', '👨‍🍳', '🍝'], color: '#D7263D',
      rounds: [
        ['Restaurant name', 'sign', [
          'The Golden Fork|Name|🍴',
          'Munch Mansion|Name|🏰',
          'Yum Yum Palace|Name|😋',
          'Flavor Town Express|Name|🚂']],
        ['Cuisine', 'room', [
          'Italian|Pasta, pizza, gelato|🇮🇹',
          'Mexican|Tacos, burritos, churros|🌮',
          'Japanese|Sushi, ramen, tempura|🍱',
          'American Diner|Burgers, shakes, fries|🍔']],
        ['Signature dish', 'room', [
          'Volcano Burger|Cheese lava pours out|🌋',
          'Rainbow Pasta|Every color noodle|🍝',
          'Dragon Roll|A sushi roll shaped like a dragon|🐉',
          'Giant Taco|Feeds a family of six|🌮']],
        ['Restaurant theme', 'room', [
          'Jungle Cafe|Vines and animal sounds|🦜',
          'Space Diner|Floating tables|🚀',
          'Pirate Ship Galley|Eat on the deck of a ship|⚓',
          'Medieval Feast Hall|Knights and torches|🛡️']],
        ['Location', 'room', [
          'On the Beach|Toes in the sand|🏖️',
          'Top of a Skyscraper|Rotates slowly|🏙️',
          'Inside a Treehouse|Up in the trees|🌳',
          'Underwater Dome|Fish swim by your table|🐟']],
        ['Dining area', 'room', [
          'Booths with Swings|Swing while you eat|🎠',
          'Ball Pit Tables|Sit in a ball pit|🔴',
          'Train Delivery Track|Food arrives by toy train|🚂']],
        ['Dessert menu', 'room', [
          'Chocolate Fountain|Dip anything|🍫',
          'Make-Your-Own Sundae Bar|Every topping|🍨',
          'Giant Cookie Pizza|Cookie the size of a pizza|🍪']],
        ['Drink menu', 'room', [
          'Bubble Tea Bar|Every flavor of boba|🧋',
          'Milkshake Bar|50 milkshake flavors|🥤',
          'Soda Fountain|Mix your own soda|🥤']],
        ['Entertainment', 'room', [
          'Live Band|Music every night|🎷',
          'Magician at Every Table|Card tricks with dinner|🃏',
          'Robot Waiters|Robots bring your food|🤖']],
        ['Special feature', 'room', [
          'Free Refills Forever|Never runs out|♾️',
          'Birthday Every Day|Free cake for everyone|🎂',
          'Rooftop Fireworks|Every Friday|🎆']]
      ]
    }
  ]);
})(window.TDA);
