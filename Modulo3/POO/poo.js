class User {
  constructor(name, age, email, password) {
    this.name = name;
    this.age = age;
    this.email = email;
    this.password = password;
    this.isLoggedIn = false;
  }

  // Metodos

  login(email, password) {
    if (this.email === email && this.password === password) {
      this.isLoggedIn = true;
      return "Login successful!";
    } else {
      return "Incorrect email or password.";
    }
  }

  logout() {
    this.isLoggedIn = false;
    return "Logout successful!";
  }
}

user1 = new User("Alice", 30, "alice@example.com", "password123");
user2 = new User("Bob", 25, "bob@example.com", "password456");

console.log(user1.email);
console.log(user1.login("alice@example.com", "password123"));
console.log(user2.login("bob@example.com", "password456"));
console.log(user1.login("alice@example.com", "wrongpassword"));
