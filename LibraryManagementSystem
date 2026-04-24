import java.util.*;
import java.time.LocalDate;
class Book
{
	private int bookId;
	private String title;
	private String author;
	boolean isIssued;
	Book(int bookId,String title,String author)
	{
		this.bookId = bookId;
		this.title = title;
		this.author = author;
		this.isIssued = false;
	}
	int getBookId()
	{
		return bookId;
	}
	String getTitle()
	{
		return title;
	}
	String getAuthor()
	{
		return author;
	}
	void setBookId(int bookId)
	{
		this.bookId = bookId;
	}
	void setTitle(String title)
	{
		this.title = title;
	}
	void setAuthor(String author)
	{
		this.author = author;
	}
}
class User
{
	private int userId;
	private String userName;
	User(int userId,String userName)
	{
		this.userId = userId;
		this.userName = userName;
	}
}
class Transaction
{
	int bookId;
	int userId;
	LocalDate issueDate;
	LocalDate dueDate;
	LocalDate returnDate;
	Transaction(int bookId,int userId)
	{
		this.bookId = bookId;
		this.userId = userId;
		this.issueDate = LocalDate.now();
		this.dueDate = issueDate.plusDays(7);
	}
	void returnBook()
	{
		this.returnDate = LocalDate.now();
	}
	long calculateFine()
	{
		if(returnDate!=null && returnDate.isAfter(dueDate))
		{
			return 200;
		}
		return 0;
	}
}
class Library
{
	List<Book> books = new ArrayList<>();
	List<User> users = new ArrayList<>();
	List<Transaction> transactions = new ArrayList<>();
	void addBook(Book book)
	{
		books.add(book);
		System.out.println("Book added successfully!");
	}
	void removeBook(int removeBookId)
	{
		for(Book i:books )
		{
			if(i.getBookId()==removeBookId)
			{
				if(i.isIssued==false)
				{
					books.remove(i);
					System.out.println("Book removed successfully!");
					return;
				}
				System.out.println("Cannot remove. the book is currently issued.");
				return;
			}
		}
		System.out.println("Book not found.");	
	}
	void searchBook(String keyWord)
	{
		for(Book i : books)
		{
			if(i.getTitle().contains(keyWord) || i.getAuthor().contains(keyWord))
			{
				System.out.println("Book found");
				System.out.println("Book ID: "+i.getBookId());
				System.out.println("Title: "+i.getTitle());
				System.out.println("Author: "+i.getAuthor());
				return;
			}	
		}
		System.out.println("Book not found.");
	}
	void updateBook(int bookId,String newTitle,String newAuthor)
	{
		for(Book i : books)
		{
			if(i.getBookId()==bookId)
			{
				i.setTitle(newTitle);
				i.setAuthor(newAuthor);
				System.out.println("Book updated successfully!");
				return;
			}
		}
		System.out.println("Book not found");
	}
	void addUser(User user)
	{
		users.add(user);
		System.out.println("User added successfully!");
	}
	void issueBook(int bookId,int userId)
	{
		for(Book i : books)
		{
			if(i.getBookId()==bookId && !i.isIssued)
			{
				i.isIssued=true;
				Transaction t = new Transaction(bookId,userId);
				transactions.add(t);
				System.out.println("Book issued successfully!");
				System.out.println("Due Date: "+t.dueDate);
				return;
			}
		}
		System.out.println("Book is not available.");
	}
	void returnBook(int bookId)
	{
		for(Transaction i : transactions)
		{
			if(i.bookId==bookId && i.returnDate ==null )
			{
				i.returnBook();
				for(Book b : books)
				{
					if(b.getBookId()==bookId)
					{
						b.isIssued = false;
					}
				}
				long fine = i.calculateFine();
				if(fine>0)
				{
					System.out.println("Fine: Rs."+fine);
				}
				System.out.println("Book returned successfully.");
				return;
			}
		}
		System.out.println("Transaction not found");
	}
}
public class Library_management_system {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Library l = new Library();
		while(true)
		{
			System.out.println("---MENU---\n1. Add Book\n2. Add User\n3. Remove Book\n4. Update Book\n5. Search Book\n6. Issue Book\n7. Return Book\n8. Exit");
			System.out.print("Enter youe choice: ");
			int choice = sc.nextInt();
			switch(choice)
			{
			case 1:
				System.out.println("Enter Book ID: ");
				int bookId = sc.nextInt();
				sc.nextLine();
				System.out.println("Enter Title: ");
				String title = sc.nextLine();
				System.out.println("Enter Author Name: ");
				String author = sc.nextLine();
				l.addBook(new Book(bookId,title,author));
				break;
			case 2:
				System.out.println("Enter User ID: ");
				int userId = sc.nextInt();
				sc.nextLine();
				System.out.println("Enter User Name: ");
				String userName = sc.nextLine();
				l.addUser(new User(userId,userName));
				break;
			case 3:
				System.out.println("Enter Book ID: ");
				int removeBookId = sc.nextInt();
				l.removeBook(removeBookId);
				break;
			case 4:
				System.out.println("Enter Book ID to Update: ");
				int updateBookId = sc.nextInt();
				sc.nextLine();
				System.out.println("Enter new Title: ");
				String newTitle = sc.nextLine();
				System.out.println("Enter new Author Name: ");
				String newAuthor = sc.nextLine();
				l.updateBook(updateBookId, newTitle, newAuthor);
				break;
			case 5:
				System.out.println("Enter keyWord: ");
				String keyWord = sc.next();
				l.searchBook(keyWord);
				break;
			case 6:
				System.out.println("Enter book ID: ");
				int issuedBookID = sc.nextInt();
				System.out.println("Enter User ID: ");
				int issuedUserId = sc.nextInt();
				l.issueBook(issuedBookID, issuedUserId);
				break;
			case 7:
				System.out.println("Enter return book ID: ");
				l.returnBook(sc.nextInt());
				break;
			case 8:
				System.out.println("Program has ended....");
				System.exit(0);
			default:
				System.out.println("Please enter valid choice");
				
			}
		}
	}

}
