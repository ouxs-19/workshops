

const houseData = [
  { name: "House Bolton", image: "/getPicture?file=House_Bolton.png" },
  { name: "House Baratheon", image: "/getPicture?file=House_Baratheon.png" },
  { name: "House Greyjoy", image: "/getPicture?file=House_Greyjoy.png" },
  { name: "House Lannister", image: "/getPicture?file=House_Lannister.png" },
  { name: "House Martell", image: "/getPicture?file=fHouse_Martell.png" },
  { name: "House Redwyne", image: "/getPicture?file=House_Redwyne.png" },
  { name: "House Stark", image: "/getPicture?file=House_Stark.png" },
  { name: "House Targaryen", image: "/getPicture?file=House_Targaryen.png" },
  { name: "House Tully", image: "/getPicture?file=House_Tully.png" },
];

	

const quotes = [
  { quote: "Our Blades Are Sharp" },
  { quote: "Ours is the Fury" },
  { quote: "What Is Dead May Never Die" },
  { quote: "A Lannister Always Pays His Debts" },
  { quote: "Unbowed, Unbent, Unbroken" },
  { quote: "Ripe for Victory" },
  { quote: "Winter is Coming" },
  { quote: "Fire and Blood" },
  { quote: "Family, Duty, Honor" },
];

houseData.forEach((house, index) => {
  house.quote = quotes[index];
});


const resolvers = {
  Query: {
    houses: () => houseData,
    randomHouse: () => {
      const randomIndex = Math.floor(Math.random() * houseData.length);
      return houseData[randomIndex];
    }
    
  },
};

module.exports = resolvers;
