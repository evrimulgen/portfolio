from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils.timezone import get_current_timezone
from django_mailbox.models import Message
import factory

from crm import models
from home.factories import TagFactory, ProjectPageFactory


class CityFactory(factory.DjangoModelFactory):
    name = factory.Faker('city')

    class Meta:
        model = models.City


class ChannelFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"channel {n}")
    url = factory.Faker('uri')

    class Meta:
        model = models.Channel


class BaseCompanyFactory(factory.DjangoModelFactory):
    name = factory.Faker('company')
    location = factory.SubFactory(CityFactory)
    channel = factory.SubFactory(ChannelFactory)
    url = factory.Faker('uri')

    class Meta:
        abstract = True


class RecruiterFactory(BaseCompanyFactory):
    class Meta:
        model = models.Recruiter


class ClientCompanyFactory(BaseCompanyFactory):
    class Meta:
        model = models.ClientCompany


class EmployeeFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    telephone = factory.Faker('phone_number')

    company = factory.SubFactory(RecruiterFactory)
    email = factory.Faker('email')

    class Meta:
        model = models.Employee


class ProjectFactory(factory.DjangoModelFactory):
    company = factory.SubFactory(ClientCompanyFactory)
    manager = factory.SubFactory(EmployeeFactory)
    location = factory.SubFactory(CityFactory)
    original_description = factory.Faker('paragraphs')
    original_url = factory.Faker('uri')
    notes = factory.Faker('text')
    daily_rate = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    start_date = factory.Faker('future_datetime', end_date="+30d")

    class Meta:
        model = models.Project

    @factory.post_generation
    def end_date(self, *args, **kwargs):
        if self.start_date:
            self.end_date = self.start_date + timedelta(days=90)


class MailboxFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"mailbox {n}")
    uri = factory.LazyAttribute(lambda x: f"imap+ssl://testusername:password@testserver")
    from_email = factory.Faker('email')

    class Meta:
        model = models.Mailbox


class MessageFactory(factory.DjangoModelFactory):
    mailbox = factory.SubFactory(MailboxFactory)
    subject = factory.Faker('sentence', nb_words=6, variable_nb_words=True)

    class Meta:
        model = Message


class ProjectMessageFactory(factory.DjangoModelFactory):
    project = factory.SubFactory(ProjectFactory)
    author = factory.SubFactory(EmployeeFactory)
    message = factory.SubFactory(MessageFactory)

    class Meta:
        model = models.ProjectMessage


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user{n}")

    class Meta:
        model = get_user_model()


class AdminFactory(UserFactory):
    is_staff = True
    is_superuser = True


class CVFactory(factory.DjangoModelFactory):
    project = factory.SubFactory(ProjectFactory)
    earliest_available = factory.Faker('past_date', start_date="-15d", tzinfo=get_current_timezone())
    full_name = factory.Faker('name')
    title = factory.Faker('sentence')
    experience_overview = factory.Faker('text')
    education_overview = factory.Faker('text')
    contact_details = factory.Faker('phone_number')
    rate_overview = "100 schmeckles"
    working_permit = "permanent"

    class Meta:
        model = models.CV


class CVWithRelevantFactory(CVFactory):

    @factory.post_generation
    def relevant_skills(self, created, extracted, **kwargs):
        if extracted:
            raise NotImplementedError()
        self.relevant_skills.set([TagFactory()])

    @factory.post_generation
    def relevant_projects(self, created, extracted, **kwargs):
        if extracted:
            raise NotImplementedError()
        self.relevant_project_pages.set([ProjectPageFactory()])
