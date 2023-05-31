from datetime import date

from schemas import (
    RecentTechnologyCategory,
    PersonalProject,
    OpenSourceContribution,
    Experience,
    Education,
    Resume,
)

recent_technology_categories = [
    RecentTechnologyCategory(
        title="Frontend",
        technologies=[
            "Typescript",
            "React",
            "Redux",
            "Apollo",
            "Tailwind",
            "GraphQL",
            "Ethers",
            "Next.js",
        ],
    ),
    RecentTechnologyCategory(
        title="Backend",
        technologies=[
            "Django",
            "Django Rest Framework",
            "Python",
            "Flask",
            "PyTest",
            "Celery",
            "Node.js",
            "Express",
            "OpenAPI",
        ],
    ),
    RecentTechnologyCategory(
        title="Infrastructure",
        technologies=[
            "Docker",
            "PostgreSQL",
            "MySQL",
            "MongoDB",
            "Redis",
            "Cloudflare Workers",
            "RabbitMQ",
            "Celery",
            "AWS",
        ],
    ),
    RecentTechnologyCategory(
        title="Third-party services",
        technologies=["Sentry", "LogRocket", "NewRelic", "ElasticSearch"],
    ),
    RecentTechnologyCategory(title="Other", technologies=["Git", "Linux"]),
]

my_personal_projects = [
    PersonalProject(
        title="Irish Rail REST API",
        description="An unofficial REST API for the Irish Rail Realtime API. The current API returns XML across a series of inconsistently named SOAP endpoints and it's not very user-friendly. I used Flask to make a self-documenting OpenAPI REST API around it, making it easier to interact with and get a view of how the different endpoints relate to each other.",
        link="https://github.com/Briscoooe/irish-rail-json-api",
        technologies=["Python", "Flask", "OpenAPI"],
    ),
    PersonalProject(
        title="Tools",
        description="This is a collection of tools I find myself needing often. The motivation for this project is to not have to trust or depend on any online service, particularly string manipulation tools on data which may be sensitive. The project is 100% dependency free. It is completely static using only HTML, CSS, and JavaScript. There is no frameworks or build process and there is no network activity.",
        link="https://briscoooe.github.io/tools/",
        technologies=["HTML", "CSS", "JavaScript"],
    ),
    PersonalProject(
        title="Discogrify",
        description="The service allows you to search for an artist on Spotify and then generate a playlist containing that artist's entire Spotify discography. This functionality is not possible using Spotify's native UI, so I took it upon myself to make it.",
        link="https://github.com/Briscoooe/Discogrify/",
        technologies=["Vue", "Go", "Spotify API"],
    ),
    PersonalProject(
        title="Hashtag Swag",
        description="A Twitter bot that generates real, purchasable t-shirts based on currently trending hashtags. Use of an on-demand clothing printing service allows customers to buy t-shirts without me ever handling them.",
        link="",
        technologies=["Python", "Tweepy", "Printful API"],
    ),
]

my_open_source_contributions = [
    OpenSourceContribution(
        title="jrnl",
        description="jrnl is a journal application for the command line. I made a fix for a bug I noticed where blank entries were being saved when they shouldn't have been.",
        link="https://github.com/jrnl-org/jrnl/pull/1653/",
    ),
    OpenSourceContribution(
        title="Leechblock",
        description="Made a quality of life improvement to the Leechblock Chrome extension. The extension allows you to block websites for a certain amount of time. The improvement was to automatically focus on the number input element when the popup is opened.",
        link="https://github.com/proginosko/LeechBlockNG/pull/286/",
    ),
    OpenSourceContribution(
        title="Docker (docs)",
        description="Updated the documentation for the Python SDK to use Python3 syntax instead of Python2.",
        link="https://github.com/docker/docs/pull/16619/",
    ),
    OpenSourceContribution(
        title="RedReader",
        description="RedReader is an unofficial, open source Android client for Reddit. I made a fix for a bug I noticed where whitespace comments would not appear properly in the app.",
        link="https://github.com/QuantumBadger/RedReader/pull/593/",
    ),
]


my_experiences = [
    Experience(
        company="One Purpose",
        title="Co-Founder and Lead Engineer",
        start_date=date(2021, 11, 1),
        end_date=date(2023, 4, 1),
        skills=[
            "Python/Django",
            "React/Typescript",
            "Postgres",
            "AWS (EB, Amplify, Lambda, SQS, S3, CDK)",
        ],
        summary="""Career management made relevant. Most human resource software is outdated and doesn't work for the individual or the manager. We make it relevant for the world we live in today.
        
            - Building and managing entire technical infrastructure and related web services for the platform
            - Communicating with early customers to gather feedback and iterate on platform features
            - Working with external design agency to assist in product design lifecycle
        """,
        location="Dublin, County Dublin, Ireland",
    ),
    Experience(
        company="Mello - DeFi onboarding made easy",
        title="Co-Founder and Lead Engineer",
        start_date=date(2021, 11, 1),
        end_date=date(2022, 6, 1),
        skills=["React/Typescript", "GraphQL", "Ethers.js", "Ethereum/Polygon"],
        summary="""Making DeFi easy to use. Simple.
        
            - Wrote entire app with integrations to Polygon, Aave, Paraswap, Ren, Balancer
            - Worked directly with UI/UX contractors on frontend overhaul
            - Successfully awarded a grant from Polygon and Aave
        """,
        location="Dublin, County Dublin, Ireland",
    ),
    Experience(
        company="On The Stage",
        title="Lead Engineer",
        start_date=date(2020, 12, 1),
        end_date=date(2021, 11, 1),
        skills=[
            "NodeJS",
            "Typescript",
            "MySQL",
            "MongoDB",
            "AWS (Lambda, API GW, SQS, EB, RDS, IAM)",
            "Redis",
            "Docker",
            "Linux",
            "Angular",
            "React",
        ],
        summary="""Planning out features and product roadmap with product manager while leading a team of two engineers, focusing on scaling efforts and long-term projects.
        
            - Planning out features and product roadmap with product manager while leading a team of two engineers, focusing on scaling efforts and long-term projects
            - Acting as a contact point for external partners and resources
        """,
        location="Remote",
    ),
    Experience(
        company="On The Stage",
        title="Software Engineer",
        start_date=date(2017, 11, 1),
        end_date=date(2020, 12, 1),
        skills=[
            "NodeJS",
            "Typescript",
            "MySQL",
            "MongoDB",
            "AWS (Lambda, API GW, SQS, EB, RDS, IAM)",
            "Redis",
            "Docker",
            "Linux",
            "Angular",
            "React",
        ],
        summary="""Working as part of a two-man development team to create and maintain a group of web apps and services connected via a series of APIs.
        
            - Working as part of a two-man development team to create and maintain a group of web apps and services connected via a series of APIs
            - Managing all AWS infrastructure for the platform
            - Automated the creation and delivery of custom promotional images, removing the need for any human involvement and speeding up the process by over 95%
            - Created a centralised health check system to provide alerts for any data inconsistencies across various internal and external services, drastically reducing the number of unknown system issues
            - Implemented an automated email marketing system, allowing clients to increase their ticket sales by up to 10%
            - Built a lead generation system that produces high quality, qualified leads and feeds them into a CRM, increasing lead quality and ARPU

        """,
        location="Greater New York City Area",
    ),
    Experience(
        company="Verizon Connect",
        title="Software Engineer",
        start_date=date(2016, 11, 1),
        end_date=date(2017, 10, 1),
        skills=[
            "C#/.NET",
            "SQL",
            "PowerShell",
            "Winforms/WPF",
            "AWS",
            "Redis",
            "RabbitMQ",
            "Docker",
            "Moq",
            "Autofac",
        ],
        summary="""Fleetmatics (acq. Verizon Connect) is a company that creates products enabling GPS tracking of fleets of vehicles. I joined just after the Verizon takeover which made it a very exciting and fast paced environment. I work in C# back-end development, primarily focused on microservices situated at the heart of the various Fleetmatics products.
            I am responsible for designing, implementing, and testing software components and other projects. Other projects exist in areas such as decoupling and migration of existing services and tools in the codebase. I also adhere to industry standards in regards to version control (Git and SVN), testing, Kanban, issue tracking, and code quality.""",
        location="County Dublin, Ireland",
    ),
]
my_educations = [
    Education(
        school="Technological University Dublin",
        degree="BSc (Hons) in Computer Science",
        start_date=date(2012, 9, 1),
        end_date=date(2016, 5, 1),
    )
]


my_resume = Resume(
    name="Brian Briscoe",
    about="I am a Senior Software Engineer with extensive experience building and managing entire technical infrastructures and related web services for multiple startups. I have worked with a range of technologies, including Python/Django, React/Typescript, Postgres, AWS, GraphQL, Ethers.js, Ethereum/Polygon, NodeJS, MySQL, MongoDB, Redis, Docker, and Linux. I have also successfully managed teams, planned product roadmaps, and collaborated with external partners and resources",
    experience=my_experiences,
    education=my_educations,
    github="https://github.com/briscoooe",
    linkedin="https://www.linkedin.com/in/brianbriscoe1/",
    email="brianbriscoe06@gmail.com",
    recent_technology_categories=recent_technology_categories,
    personal_projects=my_personal_projects,
    open_source_contributions=my_open_source_contributions,
)
