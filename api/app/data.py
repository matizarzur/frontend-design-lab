from faker import Faker

from .models import Product, Task, User

fake = Faker()
Faker.seed(42)


def _generate_users(count: int) -> list[User]:
    users = []
    for i in range(1, count + 1):
        users.append(
            User(
                id=i,
                name=fake.name(),
                email=fake.email(),
                avatar_url=f"https://i.pravatar.cc/150?img={i}",
                job_title=fake.job(),
                company=fake.company(),
            )
        )
    return users


def _generate_products(count: int) -> list[Product]:
    categories = ["Electrónica", "Ropa", "Hogar", "Deportes", "Libros"]
    products = []
    for i in range(1, count + 1):
        products.append(
            Product(
                id=i,
                name=fake.catch_phrase(),
                description=fake.sentence(nb_words=12),
                price=round(fake.random_number(digits=3) + fake.random.random(), 2),
                image_url=f"https://picsum.photos/seed/product-{i}/400/300",
                category=fake.random_element(categories),
                in_stock=fake.boolean(chance_of_getting_true=75),
            )
        )
    return products


def _generate_tasks(count: int) -> list[Task]:
    priorities = ["low", "medium", "high"]
    tasks = []
    for i in range(1, count + 1):
        tasks.append(
            Task(
                id=i,
                title=fake.sentence(nb_words=6).rstrip("."),
                description=fake.sentence(nb_words=15),
                completed=fake.boolean(chance_of_getting_true=30),
                priority=fake.random_element(priorities),
            )
        )
    return tasks


USERS: list[User] = _generate_users(30)
PRODUCTS: list[Product] = _generate_products(30)
TASKS: list[Task] = _generate_tasks(10)
_next_task_id = len(TASKS) + 1


def next_task_id() -> int:
    global _next_task_id
    value = _next_task_id
    _next_task_id += 1
    return value
