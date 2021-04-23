class Art:
  def __init__(self,artist,title,medium,year,owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner  
    
  def __repr__(self):
    return "{artist}. {title}. {year}. {medium}. {ownerName}, {ownerLoc}.".format(artist = self.artist,title = "\""+self.title+"\"",year = self.year,medium = self.medium,ownerName = self.owner.name,ownerLoc = self.owner.location)
    
class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listings(self, new_listing):
    self.listings.append(new_listing)
  def remove_listings(self,rem_listing):
    self.listings.remove(rem_listing)
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      
class Client:
  def __init__(self,name,location,is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def sell_artwork(self,artwork,price):
    self.price = price
    if artwork.owner == self:
      selling_art = Listing(artwork,price,self.name)
      veneer.add_listings(selling_art)
  
  def buy_artwork(self,artwork):
    if artwork.owner != self.name:
      art_listing = Listing(artwork,self.price,self.name)
    for listing in veneer.self.listings
      if listing == artwork:
        veneer.remove_listings(art_listing)
    
class Listing:
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller
    
  def __repr__(self):
    return "{art} cost: {price}".format(art = self.art, price = self.price)

veneer = Marketplace()
veneer.show_listings()

edytta = Client("Edytta Halpirt","Private Collection" ,False)
girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mondolin(Fanny Tellier)","1910","oil on canvas",edytta)
moma = Client("The MOMA","New York",True)

edytta.sell_artwork(girl_with_mandolin, "$6M")
veneer.show_listings()
