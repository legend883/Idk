/* Mode data: FOOD & ENTERTAINMENT shelf. Same format as modes-dream.js. */
(function (T) {
  T.addModes([
    {
      id: 'pizza', name: 'Dream Pizza', cat: 'food', kind: 'pizza', skin: 'pizza',
      blurb: 'Crust, sauce, cheese and wild toppings. Bake the greatest pizza in history.',
      ai: 'a giant gourmet pizza seen from above on a wooden board',
      cover: ['🍕', '🧀', '🍄'], color: '#F7931E',
      rounds: [
        ['Crust', 'crust', [
          'Stuffed Crust|Cheese hiding inside the edge|🧀|#E9A94B',
          'Deep Dish|Tall, thick and saucy|🥧|#C98A3B',
          'Thin & Crispy|Crunchy New York slice|🍕|#F0C075',
          'Garlic Butter Crust|Brushed with garlic butter|🧄|#E7B35A']],
        ['Sauce', 'sauce', [
          'Classic Tomato|Sweet and tangy|🍅|#D62828',
          'Creamy Alfredo|White, rich and garlicky|🥛|#F4EBD0',
          'BBQ Sauce|Smoky and sweet|🍖|#7F3B1E',
          'Pesto|Fresh basil green|🌿|#4C9A2A']],
        ['Cheese', 'cheese', [
          'Extra Mozzarella|Stretchy cheese pull|🧀|#FFE08A',
          'Four Cheese Blend|Four cheeses melted together|🧀|#FFD166',
          'Cheddar Melt|Sharp and orange|🟧|#F7A531']],
        ['Meat topping', 'topping', [
          'Pepperoni|Crispy little cups|🍕',
          'Bacon Bits|Smoky bacon everywhere|🥓',
          'Meatballs|Mini meatballs|🧆',
          'Chicken|Grilled chicken pieces|🍗']],
        ['Veggie topping', 'topping', [
          'Mushrooms|Sliced and roasted|🍄',
          'Bell Peppers|Red, yellow and green|🫑',
          'Black Olives|Little olive rings|🫒',
          'Sweet Corn|Golden kernels|🌽']],
        ['Wild topping', 'topping', [
          'Pineapple|The great debate|🍍',
          'Mac and Cheese|Pasta on pizza|🧀',
          'Hot Cheetos Crunch|Spicy crunchy dust|🌶️',
          'French Fries|Fries right on top|🍟']],
        ['Finishing touch', 'topping', [
          'Fresh Basil|A few green leaves|🌿',
          'Hot Honey Drizzle|Sweet with a kick|🍯',
          'Ranch Swirl|Ranch in a spiral|🥛']],
        ['Dipping sauce', 'side', [
          'Ranch Cup|The classic dip|🥛',
          'Garlic Butter Cup|Dunk that crust|🧈',
          'Marinara Cup|Extra tomato sauce|🍅']],
        ['Side', 'side', [
          'Garlic Knots|Buttery twisty bread|🥖',
          'Buffalo Wings|Hot and saucy|🍗',
          'Mozzarella Sticks|Cheese pull guaranteed|🧀']],
        ['Drink', 'side', [
          'Ice-Cold Soda|Fizzy and cold|🥤',
          'Lemonade|Fresh squeezed|🍋',
          'Chocolate Milk|Big glass|🥛']],
        ['Dessert pizza', 'side', [
          'Cinnamon Sticks|With icing dip|🥨',
          'Cookie Pizza|One giant cookie|🍪',
          'Brownie Bites|Warm and gooey|🍫']]
      ]
    },
    {
      id: 'fast-food', name: 'Dream Fast-Food Order', cat: 'food', kind: 'spread', skin: 'tray',
      blurb: 'Burger, fries, shake and the toy. Build the ultimate drive-thru order.',
      ai: 'an overflowing fast food meal on a red tray',
      cover: ['🍔', '🍟', '🥤'], color: '#ED1C24',
      rounds: [
        ['Main', 'meal', [
          'Triple Stack Burger|Three patties, three cheeses|🍔',
          'Crispy Chicken Sandwich|Crunchy and juicy|🥪',
          'Hot Dog Deluxe|Footlong with everything|🌭',
          'Chicken Nugget Bucket|Fifty nuggets|🍗']],
        ['Fries', 'meal', [
          'Loaded Cheese Fries|Cheese and bacon on top|🍟',
          'Waffle Fries|Crispy little waffles|🧇',
          'Sweet Potato Fries|Orange and sweet|🍠']],
        ['Drink', 'meal', [
          'Giant Soda|Bigger than your head|🥤',
          'Strawberry Shake|Pink and thick|🍓',
          'Slushie|Blue raspberry brain freeze|🧊']],
        ['Sauce', 'meal', [
          'Secret Sauce|Nobody knows the recipe|🤫',
          'Honey Mustard|Sweet and tangy|🍯',
          'Every Sauce|All twelve sauces|🥫']],
        ['Extra side', 'meal', [
          'Onion Rings|Golden rings|🧅',
          'Mozzarella Sticks|Stretchy cheese|🧀',
          'Apple Slices|Something healthy, sort of|🍏']],
        ['Snack wrap', 'meal', [
          'Spicy Chicken Wrap|With a kick|🌯',
          'Breakfast Burrito|All day breakfast|🌯',
          'Taco Box|Six crunchy tacos|🌮']],
        ['Dessert', 'meal', [
          'Apple Pie|Hot and flaky|🥧',
          'Soft Serve Cone|Swirly vanilla|🍦',
          'Cookie Sundae|Crushed cookies in ice cream|🍨']],
        ['Kids meal toy', 'meal', [
          'Robot Toy|Arms that move|🤖',
          'Mystery Plushie|Could be anything|🧸',
          'Light-Up Yo-Yo|Glows when it spins|🪀']],
        ['Upgrade', 'meal', [
          'Super Size Everything|Everything gets bigger|📏',
          'Free Refills for Life|Forever|♾️',
          'Extra Pickles|Pickles on everything|🥒']],
        ['Mystery menu item', 'meal', [
          'Burger Donut|A burger with donut buns|🍩',
          'Pizza Burger|A pizza folded into a burger|🍕',
          'Mac and Cheese Bites|Fried mac and cheese balls|🧀']]
      ]
    },
    {
      id: 'dessert-table', name: 'Dream Dessert Table', cat: 'food', kind: 'spread', skin: 'dessert',
      blurb: 'Cakes, fountains and towers of treats. Set the sweetest table ever.',
      ai: 'a giant party dessert table full of sweets',
      cover: ['🎂', '🍰', '🧁'], color: '#F15BB5',
      rounds: [
        ['Centerpiece cake', 'meal', [
          'Five-Tier Cake|Taller than a kid|🎂',
          'Unicorn Cake|Rainbow inside and out|🦄',
          'Ice Cream Cake|Frozen layers|🍰']],
        ['Fountain', 'meal', [
          'Chocolate Fountain|Dip strawberries and marshmallows|🍫',
          'Caramel Waterfall|Golden and gooey|🍯',
          'Punch Fountain|Pink fizzy punch|🍹']],
        ['Cupcakes', 'meal', [
          'Rainbow Cupcakes|Every color of frosting|🧁',
          'Red Velvet Cupcakes|Cream cheese frosting|❤️',
          'Cookie Dough Cupcakes|Cookie dough inside|🍪']],
        ['Cookies', 'meal', [
          'Giant Chocolate Chip|As big as a plate|🍪',
          'Frosted Sugar Cookies|Decorated by a pro|⭐',
          'Ice Cream Sandwiches|Cookies with ice cream|🥪']],
        ['Pie', 'meal', [
          'Apple Pie|Warm with ice cream|🥧',
          'Key Lime Pie|Tart and creamy|🍋',
          'Chocolate Cream Pie|Mountains of whipped cream|🍫']],
        ['Candy jar', 'meal', [
          'Gummy Bear Jar|Every flavor|🐻',
          'Jelly Bean Jar|Hundreds of beans|🫘',
          'Lollipop Bouquet|A bunch of giant lollipops|🍭']],
        ['Donuts', 'meal', [
          'Donut Wall|Donuts hung on pegs|🍩',
          'Cronut Tower|Croissant meets donut|🥐',
          'Mini Donut Machine|Fresh and warm|⚙️']],
        ['Frozen treat', 'meal', [
          'Sundae Bar|Make your own sundae|🍨',
          'Snow Cone Stand|Rainbow syrups|🍧',
          'Popsicle Freezer|Every flavor|🍡']],
        ['Fancy treat', 'meal', [
          'Macarons|Pastel French cookies|🍬',
          'Cream Puffs|Light and fluffy|🥟',
          'Cheesecake Bites|Tiny cheesecakes|🍰']],
        ['Surprise', 'meal', [
          'Cotton Candy Machine|Spin your own|🍭',
          'S\'mores Station|Toast marshmallows|🔥',
          'Giant Pinata|Full of candy|🪅']]
      ]
    },
    {
      id: 'candy-store', name: 'Dream Candy Store', cat: 'food', kind: 'building', skin: 'candy',
      blurb: 'Gumball machines, chocolate rivers and secret flavors. Open a sweet shop.',
      ai: 'a whimsical candy store, cutaway view',
      cover: ['🍬', '🍭', '🍫'], color: '#FF5DA2',
      rounds: [
        ['Shop name', 'sign', [
          'Sugar Rush|Name|🍬',
          'Sweet Tooth Castle|Name|🏰',
          'The Gumdrop Shop|Name|🍡',
          'Candy Kingdom|Name|👑']],
        ['Star attraction', 'room', [
          'Chocolate River|A river you can dip into|🍫',
          'Giant Gumball Machine|Two stories tall|🔴',
          'Lollipop Garden|Lollipops grow like flowers|🍭']],
        ['Chocolate counter', 'room', [
          'Truffle Wall|Hundreds of truffles|🍫',
          'Chocolate Bars of the World|Bars from every country|🌍',
          'Chocolate-Covered Everything|Pretzels, strawberries, bacon|🍓']],
        ['Gummy section', 'room', [
          'Gummy Worm Pit|Grab them by the handful|🪱',
          'Gummy Bear Tower|A tower of bears|🐻',
          'Sour Candy Station|So sour your face twists|🍋']],
        ['Classic candy', 'room', [
          'Jelly Bean Wall|Every flavor ever|🫘',
          'Taffy Puller|Watch the taffy stretch|🍬',
          'Rock Candy Crystals|Sparkling sugar crystals|💎']],
        ['Frozen treats', 'room', [
          'Ice Cream Counter|36 flavors|🍦',
          'Frozen Hot Chocolate|Cold and chocolatey|🥤',
          'Snow Cone Corner|Rainbow syrup|🍧']],
        ['Fun feature', 'room', [
          'Candy Slide|Slide into a pit of candy|🛝',
          'Candy Claw Machine|Win giant candy bars|🕹️',
          'Mystery Flavor Machine|Pull the lever, get a surprise|🎰']],
        ['Baked goods', 'room', [
          'Fudge Kitchen|Fresh fudge every hour|🍫',
          'Cookie Oven|Warm cookies all day|🍪',
          'Cupcake Window|Decorate your own|🧁']],
        ['Mascot', 'room', [
          'Gumdrop the Bear|A giant gummy bear|🐻',
          'Captain Cocoa|A chocolate pirate|🏴‍☠️',
          'Lolli the Unicorn|Rainbow lollipop horn|🦄']],
        ['Secret room', 'room', [
          'Invention Lab|Test new candy ideas|🧪',
          'Free Sample Vault|Unlimited samples|🗝️',
          'Candy Bed Lounge|Nap on marshmallows|☁️']]
      ]
    },
    {
      id: 'feast', name: 'Dream Feast', cat: 'food', kind: 'spread', skin: 'feast',
      blurb: 'A royal banquet with roasts, breads and towering desserts. Fill the great table.',
      ai: 'a royal banquet feast on a long wooden table',
      cover: ['🍗', '🥖', '🍇'], color: '#8C5E2A',
      rounds: [
        ['Main roast', 'meal', [
          'Roast Turkey|Golden and huge|🦃',
          'Glazed Ham|Honey glazed|🍖',
          'Prime Rib|Slow roasted|🥩',
          'BBQ Brisket|Smoked for 12 hours|🔥']],
        ['Bread basket', 'meal', [
          'Garlic Bread|Buttery and crunchy|🥖',
          'Warm Dinner Rolls|Fresh from the oven|🍞',
          'Cheesy Biscuits|Melty cheddar inside|🧀']],
        ['Potatoes', 'meal', [
          'Mashed Potato Mountain|With a gravy lake|🥔',
          'Loaded Baked Potatoes|Bacon, cheese, sour cream|🥔',
          'Crispy Roast Potatoes|Golden edges|🍟']],
        ['Pasta', 'meal', [
          'Giant Lasagna|Layers on layers|🍝',
          'Baked Mac and Cheese|Crunchy top|🧀',
          'Fettuccine Alfredo|Creamy noodles|🍜']],
        ['Vegetables', 'meal', [
          'Buttery Corn on the Cob|Dripping with butter|🌽',
          'Green Bean Casserole|Crispy onions on top|🫛',
          'Honey Carrots|Sweet glazed carrots|🥕']],
        ['Fruit platter', 'meal', [
          'Grape Tower|A pyramid of grapes|🍇',
          'Watermelon Basket|Carved like a basket|🍉',
          'Tropical Platter|Mango, pineapple, kiwi|🥭']],
        ['Seafood', 'meal', [
          'Shrimp Tower|Shrimp cocktail pyramid|🍤',
          'Lobster Tails|With melted butter|🦞',
          'Crab Legs|Crack and dip|🦀']],
        ['Soup', 'meal', [
          'Tomato Soup|With grilled cheese dippers|🍅',
          'Chicken Noodle|Grandma\'s recipe|🍲',
          'Clam Chowder in a Bread Bowl|Eat the bowl too|🥣']],
        ['Drinks', 'meal', [
          'Sparkling Cider|Fancy bubbles|🥂',
          'Hot Apple Cider|Cinnamon and warm|🍎',
          'Punch Bowl|Fruity and pink|🍹']],
        ['Grand dessert', 'meal', [
          'Pie Parade|Five kinds of pie|🥧',
          'Chocolate Cake Castle|A castle of cake|🏰',
          'Ice Cream Volcano|Hot fudge lava|🌋']]
      ]
    },
    {
      id: 'ice-cream', name: 'Dream Ice Cream', cat: 'food', kind: 'sundae', skin: 'sundae',
      blurb: 'Scoops, sauces, sprinkles and a cherry on top. Stack the tallest sundae.',
      ai: 'a towering ice cream sundae, close up',
      cover: ['🍦', '🍨', '🍒'], color: '#7FDBFF',
      rounds: [
        ['Cone or cup', 'base', [
          'Waffle Cone|Crunchy and sweet|🍦|cone',
          'Chocolate-Dipped Cone|Dipped in chocolate|🍫|cone-choc',
          'Giant Glass Bowl|Holds a lot|🥣|bowl',
          'Banana Split Boat|Long dish with a banana|🍌|boat']],
        ['First scoop', 'scoop', [
          'Chocolate Fudge|Rich and dark|🍫|#6B3E26',
          'Strawberry|Pink and fruity|🍓|#FF8FAB',
          'Mint Chip|Green with chocolate chips|🌿|#9FE2BF',
          'Vanilla Bean|Classic and creamy|🍦|#FFF3C4']],
        ['Second scoop', 'scoop', [
          'Cookie Dough|Chunks of dough|🍪|#E8D3A9',
          'Birthday Cake|With sprinkles inside|🎂|#FFE5EC',
          'Blue Moon|Bright blue mystery flavor|🌙|#5BC0EB',
          'Mango Sorbet|Tropical and orange|🥭|#FFB703']],
        ['Third scoop', 'scoop', [
          'Rocky Road|Marshmallows and nuts|🪨|#7B4B2A',
          'Cotton Candy|Pink and blue swirl|🍭|#CDB4DB',
          'Peanut Butter Cup|Peanut butter swirls|🥜|#C68B59',
          'Lemon Sorbet|Bright and tangy|🍋|#FFF07C']],
        ['Sauce', 'sauce', [
          'Hot Fudge|Warm chocolate pour|🍫|#3E1F0D',
          'Caramel|Golden and gooey|🍯|#C77D22',
          'Strawberry Syrup|Bright red drizzle|🍓|#D62828']],
        ['Toppings', 'topping', [
          'Rainbow Sprinkles|A sprinkle explosion|🌈',
          'Crushed Cookies|Chocolate cookie crumble|🍪',
          'Gummy Bears|A handful of gummies|🐻']],
        ['Crunch', 'topping', [
          'Chopped Peanuts|Salty crunch|🥜',
          'Cereal Crunch|Sugary cereal on top|🥣',
          'Waffle Bits|Crispy waffle pieces|🧇']],
        ['Fruit', 'topping', [
          'Sliced Strawberries|Fresh and red|🍓',
          'Banana Coins|Sweet banana slices|🍌',
          'Blueberries|A handful of blue|🫐']],
        ['Whipped cream', 'cream', [
          'Whipped Cream Tower|Extra tall swirl|☁️',
          'Marshmallow Fluff|Toasted on top|🔥',
          'Chocolate Whip|Chocolate whipped cream|🍫']],
        ['On top', 'crown', [
          'Cherry on Top|The classic finish|🍒',
          'Giant Cookie Fin|A cookie sticking up|🍪',
          'Sparkler|It is a party|🎇',
          'Mini Donut|A whole donut on top|🍩']]
      ]
    },
    {
      id: 'video-game', name: 'Dream Video Game', cat: 'food', kind: 'poster', skin: 'game',
      blurb: 'Hero, world, bosses and power-ups. Design the next must-play game.',
      ai: 'colorful video game box art',
      cover: ['🎮', '👾', '🏆'], color: '#3A0CA3',
      rounds: [
        ['Game world', 'theme', [
          'Floating Sky Islands|Islands in the clouds|☁️|#2E86AB',
          'Candy Kingdom|Everything is made of sweets|🍬|#C9184A',
          'Haunted Castle|Ghosts in every hall|🏚️|#2B193D',
          'Cyber City|Neon streets and robots|🌃|#1A0B4B']],
        ['Main character', 'lead', [
          'A Ninja Cat|Fast, sneaky, nine lives|🐱',
          'A Space Knight|Armor and a laser sword|🧑‍🚀',
          'A Skater Kid|Grinds rails everywhere|🛹',
          'A Tiny Dragon|Small but fierce|🐲']],
        ['Character ability', 'credit', [
          'Double Jump|Jump again in midair|🦘',
          'Wall Run|Run up any wall|🧱',
          'Shape Shift|Turn into animals|🦊',
          'Time Rewind|Undo mistakes|⏪']],
        ['Enemies', 'villain', [
          'Slime Goblins|Gooey and grumpy|🟢',
          'Robot Spiders|Clicky metal legs|🕷️',
          'Angry Ghosts|Float through walls|👻']],
        ['Weapon or tool', 'cast', [
          'Boomerang Sword|Always comes back|🪃',
          'Freeze Ray|Freeze anything|🧊',
          'Magic Paintbrush|Paint things into reality|🖌️']],
        ['Vehicle', 'cast', [
          'Rocket Skateboard|Super fast board|🛹',
          'Dragon Mount|Fly on a dragon|🐉',
          'Mech Suit|Giant robot armor|🤖']],
        ['Game mechanic', 'credit', [
          'Build Anything|Craft your own world|🔨',
          'Pet Collecting|Catch and train pets|🐾',
          'Racing Levels|Race between worlds|🏁']],
        ['Multiplayer', 'credit', [
          '4-Player Co-op|Team up on the couch|👥',
          '100-Player Battle|Last one standing|🪂',
          'Party Minigames|50 silly minigames|🎉']],
        ['Final boss', 'villain', [
          'The Mega Dragon|Breathes rainbow fire|🐉',
          'King Robot|Size of a skyscraper|🤖',
          'The Shadow Twin|Copies every move you make|👤']],
        ['Secret level', 'tagline', [
          'Rainbow Road|Racing on a rainbow|🌈',
          'Inside the Game Console|Fight in the wires|🔌',
          'Dinosaur Island|Ride a T-Rex|🦖']]
      ]
    },
    {
      id: 'sports-team', name: 'Dream Sports Team', cat: 'food', kind: 'team', skin: 'sports',
      blurb: 'Sign the stars, pick the mascot, build the stadium. Win the championship.',
      ai: 'a championship sports team photo with mascot and trophy',
      cover: ['🏆', '⚽', '🏀'], color: '#0077FF',
      rounds: [
        ['Sport', 'banner', [
          'Basketball|Dunks and buzzer-beaters|🏀',
          'Soccer|Goals from midfield|⚽',
          'Football|Touchdowns and tackles|🏈',
          'Baseball|Home runs every inning|⚾']],
        ['Team name', 'title', [
          'The Thunder Hawks|Name|🦅',
          'The Lava Lions|Name|🦁',
          'The Galaxy Sharks|Name|🦈',
          'The Turbo Tigers|Name|🐯']],
        ['Star player', 'member', [
          'The Rocket|Fastest player in the league|🚀',
          'The Wall|Nobody gets past|🧱',
          'The Magician|Tricks nobody can follow|🪄']],
        ['Second star', 'member', [
          'The Giant|Eight feet tall|🦒',
          'The Sniper|Never misses|🎯',
          'The Captain|Born leader|©️']],
        ['Coach', 'member', [
          'Coach Thunder|Yells, but in a nice way|📣',
          'Coach Zen|Very calm, always wins|🧘',
          'Robot Coach|Calculates every play|🤖']],
        ['Mascot', 'member', [
          'Giant Eagle|Flies over the crowd|🦅',
          'Dancing Bear|Best moves in the league|🐻',
          'Fire-Breathing Dragon|Breathes confetti|🐲']],
        ['Rookie', 'member', [
          'The Kid|12 years old and amazing|👦',
          'The Twins|Two players, one brain|👯',
          'The Mystery Player|Wears a mask, plays great|🎭']],
        ['Stadium', 'home', [
          'Dome Stadium|100,000 seats|🏟️',
          'Floating Arena|Over the ocean|🌊',
          'Volcano Field|Hot games guaranteed|🌋']],
        ['Team perk', 'member', [
          'Team Jet|Travel in style|✈️',
          'Personal Chef|Champion meals|👨‍🍳',
          'Hype DJ|Music at every game|🎧']],
        ['Celebration', 'member', [
          'Championship Parade|The whole city shows up|🎉',
          'Trophy Room|Shelves of trophies|🏆',
          'Victory Fireworks|After every win|🎆']]
      ]
    },
    {
      id: 'music-festival', name: 'Dream Music Festival', cat: 'food', kind: 'map', skin: 'festival',
      blurb: 'Stages, headliners and food trucks. Throw the festival of the summer.',
      ai: 'a huge outdoor music festival seen from above at sunset',
      cover: ['🎸', '🎤', '🎪'], color: '#F15BB5',
      rounds: [
        ['Location', 'banner', [
          'Desert Under the Stars|Huge sky, warm nights|🌵',
          'Beach Festival|Dance in the sand|🏖️',
          'Mountain Meadow|Fresh air and big views|⛰️',
          'Floating Island|Stages on the water|🏝️']],
        ['Headliner', 'spot', [
          'A Rock Legend|Guitar solos for days|🎸',
          'A Pop Superstar|Every song is a hit|🎤',
          'A DJ Robot|Drops the beat perfectly|🤖']],
        ['Main stage', 'spot', [
          'Giant Glowing Stage|Shaped like a spaceship|🛸',
          'Castle Stage|Shoots fireworks|🏰',
          'Volcano Stage|Erupts with confetti|🌋']],
        ['Opening act', 'spot', [
          'A Marching Band|Very loud, very fun|🥁',
          'A Kid Rapper|Rhymes about snacks|🧢',
          'A Barbershop Quartet|Perfect harmony|💈']],
        ['Food trucks', 'spot', [
          'Taco Truck|The best tacos ever|🌮',
          'Ice Cream Truck|Free cones all day|🍦',
          'BBQ Smoker|Ribs and brisket|🍖']],
        ['Fun zone', 'spot', [
          'Ferris Wheel|See the crowd from the top|🎡',
          'Silent Disco|Headphones on, dance off|🎧',
          'Giant Slip-n-Slide|Cool off in style|💦']],
        ['Special effect', 'spot', [
          'Laser Show|Lasers in the sky|🔦',
          'Confetti Cannons|Blast every chorus|🎊',
          'Fire Jets|Flames on the beat|🔥']],
        ['Camping', 'spot', [
          'Glamping Tents|Real beds in tents|⛺',
          'Treehouse Village|Sleep in the trees|🌳',
          'Tour Bus Hotel|Sleep in a band bus|🚌']],
        ['Merch', 'spot', [
          'Glow Sticks for All|Thousands glowing at once|🪄',
          'Custom T-Shirts|Your name on the lineup|👕',
          'Light-Up Sneakers|Shoes that dance|👟']],
        ['Grand finale', 'spot', [
          'Fireworks Over the Stage|The biggest show|🎆',
          'Drone Show Spells Your Name|In the sky|🛰️',
          'Everyone Sings Together|100,000 voices|🙌']]
      ]
    },
    {
      id: 'amusement-park', name: 'Dream Amusement Park', cat: 'food', kind: 'map', skin: 'boardwalk',
      blurb: 'A seaside boardwalk of rides, games and fried treats. Build your pier.',
      ai: 'a seaside boardwalk amusement park on a pier',
      cover: ['🎡', '🎪', '🍦'], color: '#FF7A00',
      rounds: [
        ['Big ride', 'spot', [
          'Giant Ferris Wheel|Tallest on the coast|🎡',
          'Wooden Coaster|Rattles over the ocean|🎢',
          'Sky Swings|Fly over the water|🎠']],
        ['Spin ride', 'spot', [
          'Tilt-a-Whirl|Spin and tilt|🌀',
          'Scrambler|Whips you around|💫',
          'Gravitron|Stick to the wall|🛸']],
        ['Kids ride', 'spot', [
          'Mini Train|Choo-choo around the pier|🚂',
          'Teacups|Spin as fast as you want|☕',
          'Pony Carousel|Painted ponies|🐴']],
        ['Midway game', 'spot', [
          'Ring Toss|Win a goldfish|🐟',
          'Balloon Darts|Pop to win|🎈',
          'Basketball Shootout|Three shots, big prize|🏀']],
        ['Fried treat', 'spot', [
          'Funnel Cake|Sugar snowstorm|🧁',
          'Corn Dogs|On a stick|🌭',
          'Fried Oreos|Crunchy outside, gooey inside|🍪']],
        ['Sweet stand', 'spot', [
          'Saltwater Taffy|Pulled fresh|🍬',
          'Candy Apples|Bright red and shiny|🍎',
          'Shaved Ice|Rainbow syrup|🍧']],
        ['Water fun', 'spot', [
          'Bumper Boats|Splash your friends|🚤',
          'Water Slide|Ends in the ocean|💦',
          'Splash Pad|Fountains everywhere|⛲']],
        ['Spooky spot', 'spot', [
          'Haunted House|Spooky but fun|🏚️',
          'Hall of Mirrors|Get lost laughing|🪞',
          'Fortune Teller Machine|Tells your future|🔮']],
        ['Prize booth', 'spot', [
          'Giant Teddy Bear|Taller than you|🧸',
          'Stuffed Unicorn|Rainbow mane|🦄',
          'Inflatable Banana|Why not|🍌']],
        ['Night magic', 'spot', [
          'Light-Up Pier|A million bulbs|💡',
          'Fireworks Over the Ocean|Every night|🎆',
          'Glow Parade|Floats lit up|🎇']]
      ]
    }
  ]);
})(window.TDA);
