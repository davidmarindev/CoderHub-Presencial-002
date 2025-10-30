class User
  attr_accessor :name, :email, :age

  def initialize(name, email, age, password)
    @name = name
    @email = email
    @age = age
    @password = password
    @is_logged_in = false
  end

  # Métodos

  def print_password
    @password
  end

  def login(email, password)
    if @email == email && @password == password
      @is_logged_in = true
      "Login successful!"
    else
      "Incorrect email or password."
    end
  end

  def logout
    @is_logged_in = false
    "Logout successful!"
  end
end

user1 = User.new("Alice", "alice@example.com", 30, "password123")
user2 = User.new("Bob", "bob@example.com", 25, "password456")

puts user1.email
puts user1.print_password
puts user1.login("alice@example.com", "password123")
puts user2.login("bob@example.com", "password456")
puts user1.login("alice@example.com", "wrongpassword")