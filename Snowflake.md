Snowflake Study Notes

#snowflakecerts 

  

  

Snowflake security network architecture

  

All internet communication between users and Snowflake is secured and encrypted using TLS 1.2 or higher. Snowflake also supports IP address whitelisting to enable customers to restrict access to the Snowflake service by only trusted networks.

  

Data encryption and key management Snowflake uses strong AES 256-bit encryption with a hierarchical key model rooted in a cluster of hardware security modules. 

  

All Snowflake network connectivity architectures include five basic connections: 

1. The connection between the Snowflake driver/connector and theSnowflake account URL, e.g.acme.us-east-1.snowflakecomputing.com 

2. The connection between the Snowflake driver/connector and one or moreOCSP providers,e.g.ocsp.digicert.com 

3. The connection between the Snowflake driver/connector and theSnowflake Internal Stage,e.g.randomname1stg.blob.core.windows.net 

4. The connection between the Snowflake service and the customer-owned cloud storage, e.g.a customer’s GCS Bucket 

5. The connection between the users’ browsers and theSnowflake Apps layer, e.g. apps.snowflake.com

  

  

  

  

  

**SSO with Azure Private Link**

**Client Redirect with Azure Private Link**[¶](https://docs.snowflake.com/en/user-guide/privatelink-azure#using-client-redirect-with-azure-private-link)

 **Replication & Tri-Secret Secure with Private Connectivity**

Configure the CIDR block range to block public access to Snowflake using **_your organization’s IP address range_**.

  

Sure, here are 10 multiple-choice questions related to Snowflake REST API:

  

**1. How is authentication typically handled in Snowflake REST API?**

   a. API key

   b. Username and password

   c. OAuth

   d. All of the above

  

**2. What is the primary purpose of the Snowflake REST API?**

   a. Data visualization

   b. Query execution

   c. Programmatic access to Snowflake resources

   d. Security management

  

**3. Which HTTP method is commonly used for executing SQL queries via the Snowflake REST API?**

   a. GET

   b. POST

   c. PUT

   d. DELETE

  

**4. What is the recommended format for passing parameters in a Snowflake REST API request?**

   a. Query parameters

   b. JSON body

   c. Headers

   d. URL-encoded parameters

  

**5. What role does the Snowflake Token Exchange play in the REST API authentication flow?**

   a. Obtaining OAuth tokens

   b. Handling API key exchange

   c. Verifying user credentials

   d. None of the above

  

**6. Which endpoint is commonly used for executing a SQL query in Snowflake REST API?**

   a. /query/run

   b. /execute/sql

   c. /executeQuery

   d. /sql/run

  

**7. What does the HTTP status code 429 signify in the context of Snowflake REST API?**

   a. Unauthorized

   b. Too Many Requests

   c. Internal Server Error

   d. OK

  

**8. In Snowflake REST API, how is result pagination typically managed?**

   a. Offset and limit parameters

   b. Cursor-based pagination

   c. Page number parameter

   d. Scroll API

  

**9. What is the purpose of the /v1/warehouses endpoint in Snowflake REST API?**

   a. User management

   b. Warehouse configuration

   c. Database creation

   d. Role assignments

  

**10. Which Snowflake REST API endpoint is commonly used for fetching information about a specific database object (e.g., table or view)?**

   a. /metadata/object

   b. /database/info

   c. /object/details

   d. /v1/databases/{database_name}/objects/{object_name}**

  

Feel free to answer these, and I can provide feedback or explanations if needed!

  

Here are the correct answers to the multiple-choice questions:

  

1. **Answer: c. OAuth**

  

2. **Answer: c. Programmatic access to Snowflake resources**

  

3. **Answer: b. POST**

  

4. **Answer: b. JSON body**

  

5. **Answer: a. Obtaining OAuth tokens**

  

6. **Answer: a. /query/run**

  

7. **Answer: b. Too Many Requests**

  

8. **Answer: a. Offset and limit parameters**

  

9. **Answer: b. Warehouse configuration**

  

10. **Answer: d. /v1/databases/{database_name}/objects/{object_name}**

  

Feel free to ask if you have any specific questions or need further clarification on any of the answers!

  

  

snowflake features & capabilities which can be leveraged across accounts

  

Snowflake provides various features and capabilities that can be leveraged across multiple accounts. These features are designed to enhance collaboration, data sharing, and resource optimization. Here are some key features and capabilities in Snowflake that can be utilized across accounts:

- **Data Sharing:**

- **Secure Data Sharing:** Snowflake allows for secure and governed data sharing between different accounts. Data can be shared seamlessly across organizational boundaries while maintaining control over access and permissions.

- **Cross-Account Access:**

- **Cross-Account Data Access:** Users in one Snowflake account can access data in another account through secure configurations, enabling collaboration and integration between different business units or partners.

- **External Functions:**

- **External Functionality:** Snowflake supports the use of external functions, allowing users to execute code or functions in external systems (e.g., AWS Lambda, Azure Functions) directly from Snowflake. This can be useful for cross-account integration.

- **Cross-Region Data Replication:**

- **Multi-Region Replication:** Snowflake enables replication of data across different regions, providing geographical redundancy and facilitating data access for users across the globe.

- **Data Exchange:**

- **Snowflake Data Exchange:** The Snowflake Data Exchange allows organizations to discover and access third-party data sets. This can be beneficial for sharing or monetizing data assets across accounts.

- **Multi-Cloud Support:**

- **Multi-Cloud Deployments:** Snowflake is designed to work across multiple cloud providers (AWS, Azure, Google Cloud). This allows organizations to leverage the strengths of different cloud platforms for specific use cases or to accommodate multi-cloud strategies.

- **Resource Sharing:**

- **Resource Sharing across Warehouses:** Organizations can share computing resources by allowing one account to use the virtual warehouses of another account. This can be useful for optimizing resource utilization and cost management.

- **Security and Governance:**

- **Cross-Account Security Policies:** Security policies, user roles, and access controls can be defined and enforced across multiple accounts, ensuring consistent security measures and governance.

- **Cross-Account Monitoring:**

- **Account Usage Metrics:** Snowflake provides account-level metrics and monitoring that can be accessed centrally, facilitating performance analysis and optimization across different accounts.

- **Data Privacy and Compliance:**

- **Data Masking and Redaction:** Snowflake supports data masking and redaction policies that can be applied consistently across accounts, ensuring compliance with privacy regulations.

When leveraging these features across accounts, it's essential to follow best practices for security, access controls, and governance to maintain a secure and well-managed data environment. Always refer to the latest Snowflake documentation for detailed information on each feature and its configuration options.

  

  

  

features in difference snowflake editions in supporting of PCI standards, PHI, PII

  

ChatGPT

**ChatGPT**

As of my last knowledge update in January 2022, Snowflake does not have different editions in the traditional sense like some other database systems. Snowflake operates as a cloud-native data platform and follows a consumption-based pricing model where users pay for the resources they consume. However, Snowflake does offer different service tiers that cater to different performance and resource requirements:

- **Standard Edition:**

- This is the default edition and provides standard performance with multi-cluster, auto-scaling compute resources.

- **Enterprise Edition:**

- Offers additional features such as enhanced performance, advanced security features, and support for features like geographically distributed data.

- **Business Critical Edition:**

- Designed for high-performance workloads, this edition includes all the features of the Enterprise Edition with additional performance optimizations.

Regarding support for PCI standards, PHI (Protected Health Information), and PII (Personally Identifiable Information), Snowflake provides a range of security features that help organizations comply with various regulatory requirements, including those related to data protection and privacy. Some relevant features include:

- **Encryption:**

- Snowflake encrypts data in transit and at rest by default. It supports TLS/SSL for securing data in transit and provides automatic encryption for data stored in the cloud.

- **Role-Based Access Control (RBAC):**

- Snowflake allows users to define roles and assign granular permissions to control access to databases, schemas, tables, and other objects. This helps in enforcing the principle of least privilege.

- **Data Masking and Redaction:**

- Snowflake provides data masking and redaction capabilities, allowing organizations to control the visibility of sensitive information based on user roles and privileges.

- **Audit Logging:**

- Snowflake offers extensive audit logging capabilities, allowing organizations to track and monitor user activities. This is crucial for compliance with regulatory standards.

- **Secure Data Sharing:**

- Snowflake's data sharing feature allows organizations to securely share data across accounts, facilitating collaboration while maintaining control over access.

- **External Tokenization:**

- Snowflake supports external tokenization, which allows users to tokenize sensitive data before loading it into Snowflake, enhancing security.

- **Data Classification and Discovery:**

- Snowflake supports data classification and discovery tools to help identify and manage sensitive data within the platform.

  

  

MFA A cached MFA token is valid for up to four hours.

  

REST API for Snowpipe workflow

  

  

  

  

**Compliance Certifications:**

- Snowflake may achieve various compliance certifications, including but not limited to PCI DSS, SOC 2, and HIPAA. The specific certifications may vary based on the edition and configuration.

  

  

**Regulatory compliance**

Snowflake is committed to meeting industry-standard regulatory compliance requirements to provide our customers the highest levels of assurance for data integrity, security, and governance.

This topic is a reference for Snowflake certifications based on geographic regions.

**Global**

- [ISO-27001](https://docs.snowflake.com/en/user-guide/cert-iso-27001)

- [ISO-27017](https://docs.snowflake.com/en/user-guide/cert-iso-27017)  
    
- [ISO-27018](https://docs.snowflake.com/en/user-guide/cert-iso-27018)  
    

- [SOC 1 Type II](https://docs.snowflake.com/en/user-guide/cert-soc-1)  
    
- [SOC 2 Type II](https://docs.snowflake.com/en/user-guide/cert-soc-2)  
    

**U.S. Government**

- [CJIS (Criminal Justice Information Services)](https://docs.snowflake.com/en/user-guide/cert-cjis)  
    
- [FedRAMP](https://docs.snowflake.com/en/user-guide/cert-fedramp)  
    
- [ITAR](https://docs.snowflake.com/en/user-guide/cert-itar)  
    
- [StateRAMP](https://docs.snowflake.com/en/user-guide/cert-stateramp)  
    

**Healthcare and life sciences**

- [HITRUST CSF](https://docs.snowflake.com/en/user-guide/cert-hitrust)  
    

**Financial services**

- [PCI-DSS](https://docs.snowflake.com/en/user-guide/cert-pci-dss)  
    

**Regional — Australia**

- [IRAP (Protected)](https://docs.snowflake.com/en/user-guide/cert-irap)
-   
    

  

  

  

  
OAuth

  

Currently, Snowflake OAuth supports the following applications:

|   |   |   |
|---|---|---|
|**Client**|**Required Client Version**|**Client Type**|
|[Tableau Desktop / Server / Online](https://www.tableau.com/) [[1]](https://docs.snowflake.com/user-guide/oauth-partner#id3)|2019.1 or higher|Public|
|[Looker](https://looker.com/) [[2]](https://docs.snowflake.com/user-guide/oauth-partner#id4)|6.20 or higher||
|[Alation](https://www.alation.com/)|See the [Alation documentation](https://docs.snowflake.com/user-guide/oauth-partner#label-snowflake-oauth-login-alation)||
|[ThoughtSpot](https://thoughtspot.com/)|See the [ThoughtSpot documentation](https://docs.snowflake.com/user-guide/oauth-partner#label-snowflake-oauth-login-thoughtspot)||
|[Collibra](https://www.collibra.com/)|See the [Collibra documentation](https://docs.snowflake.com/user-guide/oauth-partner#label-snowflake-oauth-login-collibra)||

  

Workflow for Kafka connector for Snowpipe

  

  

  

Kafka connector with Snowpipe streaming

**5 Practice Exams | COF-CO2 SNOWFLAKE CORE**

#snowflakecerts 

  

**EXAM - 1**

**Question 3**

Incorrect

Which category of privileges does the MONITOR TASK privilege belong to?

Choose **one** correct answer.

  

Schema-level Privileges

Explanation

Schema-level privileges control operations on schemas themselves, such as CREATE, USAGE, or MODIFY, but not on the objects within the schema.

**Your answer is incorrect**

  

Account Object Privileges

Explanation

These apply to high-level objects like resource monitors, virtual warehouses, and databases, not tasks.

**Correct answer**

  

Schema Object Privileges

Explanation

Tasks are schema objects, just like tables, views, or procedures. Therefore, privileges that apply to tasks — including MONITOR TASK — are classified under "Schema Object Privileges."

  

Global Privileges

Explanation

Global privileges apply across the account, like MANAGE GRANTS or MONITOR USAGE, not specific to tasks.

Overall explanation

In Snowflake, objects are organised hierarchically, and tasks are a type of schema object, meaning they exist inside a specific schema.

  

  

  

As a result, the privileges that apply to **tasks** are part of the “Schema Object Privileges” category.

For example, to monitor a scheduled task's execution history or status, a user must have the MONITOR privilege on the task object itself. This is similar to how SELECT works for tables or EXECUTE works for stored procedures — these all fall under schema object privileges.

Here’s an example of granting this privilege:

- GRANT MONITOR ON TASK my_schema.my_task TO ROLE analyst_role;

This structure keeps access control fine-grained, so users can be given rights to monitor specific tasks without affecting global settings or other account-level resources.

  

  

**Question 10** 

Explanation

You can assign a **maximum of 50 unique tags** to a single object in Snowflake (like a table, view, or stage). This limit applies to the number of **distinct tags**, not the number of tag/value combinations. For example, you could apply the same tag to multiple columns with different values, and that would still count as **one tag**.

Overall explanation

Snowflake allows up to 50 unique tags on an object, like a table or view, and another 50 tags total across all columns in that object. This limit is on the number of different tags, not the number of tag/value combinations. If you hit the tag limit, you’ll need to remove a tag using UNSET TAG before adding more. You can specify up to 100 tags in a single CREATE or ALTER statement, as long as they don’t exceed the object-level or column-level limits.

  

Question 14

APPROX_COUNT_DISTINCT

Explanation

APPROX_COUNT_DISTINCT is designed to efficiently estimate the number of distinct elements using the **HyperLogLog** algorithm.

Overall explanation

In Snowflake, if you're looking to get a **fast, approximate count of unique values** — also called cardinality estimation — you should use APPROX_COUNT_DISTINCT(). This function is particularly useful for big data scenarios where performance is critical and **a small margin of estimation error is acceptable**.

For example:

- SELECT APPROX_COUNT_DISTINCT(user_id) FROM user_activity;

This would return an approximate number of unique users. It’s much more efficient than COUNT(DISTINCT user_id) when working with millions or billions of rows.

The approximation is made possible by the **HyperLogLog** algorithm, a probabilistic technique that enables counting large numbers of distinct values with minimal memory use. This makes it ideal for dashboards, reports, or exploratory analysis where speed matters more than exact precision.

**Resources**

  

  

APPROX_COUNT_DISTINCT

Explanation

APPROX_COUNT_DISTINCT is designed to efficiently estimate the number of distinct elements using the **HyperLogLog** algorithm.

Overall explanation

In Snowflake, if you're looking to get a **fast, approximate count of unique values** — also called cardinality estimation — you should use APPROX_COUNT_DISTINCT(). This function is particularly useful for big data scenarios where performance is critical and **a small margin of estimation error is acceptable**.

For example:

- SELECT APPROX_COUNT_DISTINCT(user_id) FROM user_activity;

This would return an approximate number of unique users. It’s much more efficient than COUNT(DISTINCT user_id) when working with millions or billions of rows.

The approximation is made possible by the **HyperLogLog** algorithm, a probabilistic technique that enables counting large numbers of distinct values with minimal memory use. This makes it ideal for dashboards, reports, or exploratory analysis where speed matters more than exact precision.

**Resources**

  

**APPROX_COUNT_DISTINCT**

Uses HyperLogLog to return an approximation of the distinct cardinality of the input (i.e. HLL(col1, col2, ... ) returns an approximation of COUNT(DISTINCT col1, col2, ... )).

For more information about HyperLogLog, see [Estimating the Number of Distinct Values](https://docs.snowflake.com/en/user-guide/querying-approximate-cardinality).

**Aliases:**

[HLL](https://docs.snowflake.com/en/sql-reference/functions/hll).

**See also:**

[HLL_ACCUMULATE](https://docs.snowflake.com/en/sql-reference/functions/hll_accumulate) , [HLL_COMBINE](https://docs.snowflake.com/en/sql-reference/functions/hll_combine) , [HLL_ESTIMATE](https://docs.snowflake.com/en/sql-reference/functions/hll_estimate)

  

  

**Question 18**

Incorrect

Which parameter is **incompatible** with the AT keyword when selecting data from a specific point in the past?

Choose **one** correct answer.

**Correct answer**

  

DATE

Explanation

DATE is not a valid parameter for the AT clause on its own. You must cast it to a TIMESTAMP type like TIMESTAMP_NTZ, TIMESTAMP_LTZ, or TIMESTAMP_TZ to use it in Time Travel.

**Your answer is incorrect**

  

STATEMENT

Explanation

STATEMENT is valid and refers to a specific query ID, so you can view the data state just after that statement was executed.

  

TIMESTAMP

Explanation

TIMESTAMP is fully supported with the AT clause. It allows you to query data as it existed at a specific point in time.

  

OFFSET

Explanation

OFFSET lets you specify how far back in time to look (e.g., OFFSET => -60*5 for 5 minutes ago). It’s compatible with the AT keyword.

Overall explanation

Snowflake’s Time Travel feature allows you to query historical data from a table or view as it existed at a specific point in the past using the AT or BEFORE clause. These clauses are placed in the FROM clause and accept parameters such as TIMESTAMP, OFFSET, or STATEMENT.

However, a plain DATE value is not valid. If you want to use a calendar date (like '2024-06-05'), to prevent the query failing you must explicitly cast it to a supported timestamp type (TIMESTAMP_LTZ, TIMESTAMP_NTZ, or TIMESTAMP_TZ).

Here are a few examples:

Query using a specific timestamp:

- SELECT * 
- FROM my_table 
- AT(TIMESTAMP => '2024-06-26 09:20:00 -0700'::TIMESTAMP_LTZ);

Query data as it was 5 minutes ago:

- SELECT * 
- FROM my_table 
- AT(OFFSET => -60*5);

Query just before a specific query executed:

- SELECT * 
- FROM my_table 
- BEFORE(STATEMENT => '8e5d0ca9-005e-44e6-b858-a8f5b37c5726');

  

  

**Question 20**

Incorrect

Which of the following are true about clustering keys in Snowflake?

Choose **two** correct answers.

  

A table can have a maximum of 10 clustering keys

Explanation

Snowflake does not impose a strict limit like 10. However, it recommends using no more than **3 or 4** columns to avoid unnecessary complexity and cost in clustering maintenance.

  

Clustering keys can only be defined at table creation

Explanation

Clustering keys **can be added or changed later** using the ALTER TABLE ... CLUSTER BY command. You are not limited to defining them only at creation.

**Your selection is correct**

  

Clustering keys co-locate data in micro-partitions for better micro-partition pruning

Explanation

Clustering keys logically order data within micro-partitions to improve query performance by enabling more effective micro-partition pruning. This is done by sorting rows within micro-partitions based on the clustering key columns, allowing Snowflake to skip scanning partitions that don’t match query filter conditions.

**Correct selection**

  

Useful for WHERE and JOIN clauses

Explanation

Clustering keys are especially effective when used on columns that frequently appear in WHERE, JOIN, GROUP BY, or ORDER BY clauses, as this boosts partition pruning and improves query efficiency.

  

Clustering keys eliminate the need for pruning

Explanation

**Clustering keys support partition pruning** — they do not eliminate the need for it. Snowflake always attempts to prune partitions; clustering simply helps make pruning more precise and effective.

Overall explanation

Clustering keys in Snowflake define how data is logically ordered within a table’s micro-partitions. By organising rows based on specified columns or expressions, they enhance **query performance** through more efficient **micro-partition pruning**, which allows Snowflake to skip scanning data that doesn’t match filter conditions. This is especially beneficial for large tables that are frequently queried using selective filters on the clustered columns.

Clustering keys can be added either at table creation or afterwards using ALTER TABLE:

- -- Add or change clustering key on an existing table
- ALTER TABLE orders CLUSTER BY (created_at, customer_id);

While there is no hard limit to the number of clustering columns, Snowflake recommends using no more than 3–4 to balance pruning effectiveness with the cost of maintaining the clustering structure. Clustering is typically most beneficial when tables are queried more often than they are updated, due to the compute and storage costs involved in reclustering.

  

  

**Question 22**

Incorrect

When querying a column of data type VARIANT what methods are used to access its elements?

Choose **two** correct answers.

  

Brace Notation

Explanation

Brace notation is not a supported syntax in Snowflake for accessing VARIANT data.

  

IS_OBJECT function

Explanation

IS_OBJECT is a predicate function used to test whether a VARIANT contains an object (e.g., JSON object), returning a boolean. It does not retrieve elements.

**Correct selection**

  

Dot Notation

Explanation

Dot notation is one way to access the elements of nested data in a semi-structured VARIANT column. Here's an example in which a dot is used to access the an element of the object order_contents: 

- SELECT src:order_contents.product_name
- FROM orders
- ORDER BY 1;

  

PARSE_VARIANT function

Explanation

There is no PARSE_VARIANT function in Snowflake.

**Your selection is correct**

  

Bracket Notation

Explanation

Bracket notation is one way to access the elements of nested data in a semi-structured VARIANT column. Here's an example in which brackets enclose the top-level element (order_contents) and one of its child elements (product_name):

- SELECT src['order_contents']['product_name']
- FROM orders
- ORDER BY 1;

Overall explanation

When working with semi-structured data in Snowflake — such as JSON stored in a VARIANT column — you often need to access nested fields. Snowflake supports two main methods: **dot notation** (e.g., column:key) and **bracket notation** (e.g., column['key']). Both approaches allow you to traverse JSON-like structures and extract values deeply nested within the object.

For example, suppose a VARIANT column named order_info contains:

- { "order_contents": { "product_name": "T-shirt", "quantity": 2 } }

You can access the product name using either:

- SELECT order_info:order_contents.product_name FROM orders;

or

- SELECT order_info['order_contents']['product_name'] FROM orders;

These notations are important tools in Snowflake when working with data formats like JSON, Avro, or Parquet.

  

**Question 23**

Incorrect

Which AWS service can be used to manage the customer-managed master key for the Tri-Secret Secure Snowflake feature?

Choose **one** correct answer.

**Your answer is incorrect**

  

AWS CloudHSM

Explanation

CloudHSM offers hardware-level key storage and cryptographic operations, but it’s not part of the supported customer-managed key setup for TSS in Snowflake.

**Correct answer**

  

AWS KMS

Explanation

AWS Key Management Service (KMS) is the correct choice for managing customer-managed keys for use with Tri-Secret Secure. It integrates directly with Snowflake’s key hierarchy and supports the self-registration process required to activate TSS.

  

Overall explanation

Tri-Secret Secure adds an extra layer of control to Snowflake’s already strong encryption model by letting you bring your own key (BYOK). In AWS, this means using **AWS Key Management Service (KMS)** to generate and manage your Customer Managed Key (CMK). This key, together with a key managed by Snowflake, forms a composite master key. If you revoke your key, Snowflake can no longer decrypt your data, offering strong data protection and ownership.

To use Tri-Secret Secure, you go through a self-registration process in Snowflake where you register your KMS key and verify connectivity. Once Snowflake support enables your account, your CMK becomes part of the encryption hierarchy.

The key management services available for each platform are:

- **AWS:** AWS Key Management Service (KMS)  
    
- **Google Cloud:** Cloud Key Management Service (Cloud KMS)  
    
- **Microsoft Azure:** Azure Key Vault  
    

**Question 27**

Incorrect

Which two of the following terms are associated specifically with a **secondary** database in a Snowflake replication setup?

Choose **two** correct answers.

  

Primary

Explanation

"Primary" refers to the source database, not the secondary replica.

  

Writable

Explanation

A secondary database is always **read-only** and cannot be written to.

**Your selection is correct**

  

Read-only

Explanation

All operations on a secondary database are **read-only**—no DML or DDL allowed.

  

Source

Explanation

"Source" describes the primary database, not the secondary one.

**Correct selection**

  

Refreshable

Explanation

Secondary databases must be **refreshed** manually or on a schedule to stay in sync with the primary.

Overall explanation

Snowflake replication lets you copy databases and other account-level objects (like roles, warehouses, and integrations) from a primary account to one or more secondary accounts. The secondary versions are read-only, but kept in sync through manual or scheduled refreshes. If you're using failover groups, you can promote a secondary to become the new primary in case of an outage.

All accounts can replicate databases and shares, but if you want to replicate things like users, roles, or network policies, or use failover, you’ll need Business Critical Edition or higher.

For example, a company might replicate its production environment in AWS US-East to a backup in Azure Europe. That secondary copy stays read-only, but if there's an issue in US-East, they can promote the Azure copy and keep operations running.

  

**Question 45**

Incorrect

Which function should be executed to obtain the Snowflake hostname IP address, and ports for private connectivity?

Choose **one** correct answer.

**Correct answer**

  

SYSTEM$ALLOWLIST_PRIVATELINK()

Explanation

This function returns hostnames and port numbers specifically needed for private connectivity services (AWS PrivateLink, Azure Private Link, Google Cloud Private Service Connect)

  

Overall explanation

When you're setting up private, secure connections to Snowflake (AWS PrivateLink, Azure Private Link, or Google Cloud Private Service Connect) you need to know exactly which Snowflake hosts and ports to let through your firewall.

You use SYSTEM$ALLOWLIST_PRIVATELINK() to generate a detailed JSON list of endpoint types (such as SNOWFLAKE_DEPLOYMENT, STAGE, OCSP_CACHE, etc.) along with their hostnames and port numbers. You can then feed this output into Snowflake’s connectivity diagnostic tool (SnowCD) to validate your network setup or manually update your firewall rules. For example:

SELECT SYSTEM$ALLOWLIST_PRIVATELINK();

returns a VARIANT containing an array of JSON objects, each including type, host, and port. Here's a example output from the Snowflake documentation:

[

{"type":"SNOWFLAKE_DEPLOYMENT", "host":"xy12345.us-west-2.privatelink.snowflakecomputing.com","port":443},

{"type":"STAGE", "host":"sfc-ss-ds2-customer-stage.s3.us-west-2.amazonaws.com","port":443},

...

{"type":"SNOWSQL_REPO", "host":"sfc-repo.snowflakecomputing.com", "port":443},

...

{"type":"OUT_OF_BAND_TELEMETRY","host":"client-telemetry.snowflakecomputing.com","port":443},

{"type":"OCSP_CACHE", "host":"ocsp.station00752.us-west-2.privatelink.snowflakecomputing.com","port":80}

]

  

  

**Question 46**

Incorrect

What method of authentication is required for using Snowpipe REST endpoints?

Choose **one** correct answer.

  

Username and password

Explanation

Snowpipe REST endpoints do not use username/password authentication.

  

API keys

Explanation

API keys are not the authentication method for Snowpipe.

**Correct answer**

  

JWT with RSA encryption

Explanation

Snowpipe REST endpoints require authentication using JSON Web Tokens (JWTs) signed with an RSA public/private key pair. This method ensures secure, token-based access to Snowflake's REST API.

  

Overall explanation

Snowpipe’s REST API uses JWTs (JSON Web Tokens) signed with RSA keys for authentication. You create a key pair, add the public key to your Snowflake user, and sign the JWT with your private key—no passwords or API keys needed. This makes things secure and ideal for automated data loads from external apps.

Here’s a quick Python example to show how it works:

- import jwt, datetime

- with open("rsa_key.p8", "rb") as f:
- private_key = f.read()

- payload = {
- "iss": "<account>.snowflakecomputing.com",
- "sub": "<snowflake_user>",
- "iat": datetime.datetime.utcnow(),
- "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
- }

- token = jwt.encode(payload, private_key, algorithm="RS256")
- headers = { "Authorization": f"Bearer {token}" }

You send this token in your request headers when calling Snowpipe’s REST endpoints (like insertReport). It’s a clean, secure way to authenticate without passing usernames or passwords.

  

🔐 **1. The idea**

Instead of sending your username/password or an API key every time you call a Snowpipe endpoint (like /insertFiles or /insertReport), Snowflake lets you **prove your identity using a signed token**.

A **JWT** is a small, digitally signed JSON object that contains:

- **Who you are** (sub)  
    
- **Who issued it** (iss)  
    
- **When it was issued / when it expires** (iat, exp)  
    

You sign it with your **private RSA key**, and Snowflake verifies it with the **public key** you uploaded to your Snowflake user profile.

  

🔑 **2. Setting it up**

You generate an RSA key pair once:

  

openssl genrsa -out rsa_key.p8 2048

openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

- Add the **public key** to your Snowflake user:  
      
      
      
    ALTER USER my_user SET rsa_public_key='MIIBIjANBgkqhkiG9...';
-   
      
      
    
- Keep the **private key** safe in your automation system (not in Git!).  
    

  

🧾 **3. Creating the token (the Python example explained)**

  

import jwt, datetime

  

with open("rsa_key.p8", "rb") as f:

    private_key = f.read()

  

payload = {

    "iss": "<account>.snowflakecomputing.com",  # your Snowflake account URL

    "sub": "<snowflake_user>",                  # the Snowflake user name

    "iat": datetime.datetime.utcnow(),          # issued at

    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)  # expires in 1h

}

  

token = jwt.encode(payload, private_key, algorithm="RS256")

headers = { "Authorization": f"Bearer {token}" }

This builds a JWT that expires after 60 minutes and is signed using your **private RSA key** with the RS256 algorithm.

  

📤 **4. Using the token**

Now you can make REST calls like:

  

curl -X GET \

  -H "Authorization: Bearer <token>" \

  https://<account>.snowflakecomputing.com/v1/data/pipes/my_pipe/insertReport

Snowflake verifies:

- The signature (with your uploaded **public key**)  
    
- The token hasn’t expired  
    
- The iss and sub match a valid Snowflake user  
    

✅ If all checks pass, your request is authenticated.

  

  

**Question 55**

Incorrect

Which ability is unique to JavaScript UDFs when compared to SQL UDFs?

Choose **one** correct answer.

**Correct answer**

  

JavaScript UDFs can call themselves recursively

Explanation

JavaScript UDFs support recursion, allowing the function to call itself as part of its logic. This is not possible with SQL UDFs.

  

**Overall explanation**

**In Snowflake, JavaScript UDFs offer greater procedural flexibility than SQL UDFs, including support for recursion—the ability of a function to call itself. This enables complex operations like traversing strings or trees step by step, which SQL UDFs cannot perform directly.**

**By contrast, SQL UDFs are purely declarative and limited to evaluating expressions. They do not support recursion or control flow constructs such as loops or conditionals.**

**Some code show a recursive JavaScript UDF:**

- CREATE OR REPLACE FUNCTION RECURSION_TEST(STR VARCHAR)
- RETURNS VARCHAR
- LANGUAGE JAVASCRIPT
- AS $$
- return (STR.length <= 1 
- ? STR 
- : STR.substring(0,1) + '_' + RECURSION_TEST(STR.substring(1)));
- $$;

- -- SELECT RECURSION_TEST('ABC'); --> Output: A_B_C

  

  

**Question 56**

Incorrect

Which command is used to disable replication for a primary database in Snowflake?

Choose **one** correct answer.

  

DISABLE REPLICATION

Explanation

This is not a valid SQL command in Snowflake.

  

SYSTEM$DISABLE_REPLICATION

Explanation

This system function does not exist in Snowflake.

**Correct answer**

  

SYSTEM$DISABLE_DATABASE_REPLICATION

Explanation

This system function is used to **disable replication** for a primary database in Snowflake. Once executed, it prevents further replication and also affects any associated secondary databases.

  

Overall explanation

To stop replication for a primary database in Snowflake, you must use the system function SYSTEM$DISABLE_DATABASE_REPLICATION. It effectively halts the sync between the primary and any secondary databases. This function ensures you're no longer incurring replication-related compute or transfer costs.

Here it is in action:

- SELECT SYSTEM$DISABLE_DATABASE_REPLICATION('my_primary_database');

This command disables replication for the database named my_primary_database.

  

  

**Question 57**

Incorrect

What happens when both a row access policy and a column-level masking policy are applied to the same table or view?

Choose **one** correct answer.

**Correct answer**

  

Row access policies are evaluated before column masking policies

Explanation

Row access policies are evaluated first before column masking policies. This means that the row access policy will determine which rows the user has access to, and then the column masking policy will further restrict the visibility of specific columns within those rows.

  

**Overall explanation**

**When both a row access policy and a column masking policy are applied to a table or view in Snowflake, they are evaluated in a specific order:**

1. Row Access Policy – Filters out any rows the user should not see.  
    
2. Column Masking Policy – Applies redaction or masking rules to specific columns in the rows the user is allowed to view.  
    

**This layered approach enforces stronger data security. For example, there’s no point in masking values in rows a user should never see in the first place.**

  

**Here’s how you might set both policies on a table:**

- -- Create a row access policy
- CREATE OR REPLACE ROW ACCESS POLICY region_policy
- AS (region STRING) RETURNS BOOLEAN ->
- CURRENT_ROLE() = 'REGIONAL_MANAGER' AND region = 'EU';

- -- Apply it to a table
- ALTER TABLE sales ADD ROW ACCESS POLICY region_policy ON (region);

- -- Create a masking policy for sensitive salary column
- CREATE OR REPLACE MASKING POLICY salary_mask
- AS (val NUMBER) RETURNS NUMBER ->
- CASE
- WHEN CURRENT_ROLE() IN ('HR') THEN val
- ELSE NULL
- END;

- -- Apply masking policy
- ALTER TABLE sales MODIFY COLUMN salary SET MASKING POLICY salary_mask;

**This setup means:**

- A user not in the 'REGIONAL_MANAGER' role won’t see any EU rows.  
    
- Even if they do see those rows, the salary column will be masked unless they’re in the HR role.

  

**Question 73Incorrect**

Which parameter in a JAVA UDF is used to store a compiled jar file for future executions?

Choose **one** correct answer.

**Your answer is incorrect**

  

handler

Explanation

The handler specifies the class and method that Snowflake will execute from the compiled JAR, but it doesn’t control how or where the JAR is stored.

  

language

Explanation

The language parameter specifies which programming language is used in the UDF (JAVA, PYTHON, etc.), but it does not deal with file storage or compilation output.

**Correct answer**

  

target_path

Explanation

The TARGET_PATH parameter stores the compiled JAR file on a stage so it can be reused for future executions without recompiling. This improves performance and supports better code management.

  

Overall explanation

In Snowflake, when you define a Java UDF with in-line code, Snowflake compiles it into a JAR file. By default, this JAR is temporary. To persist it for reuse and avoid recompilation, use the TARGET_PATH parameter to store the compiled JAR in a stage (e.g., @handlers/…). This enables performance improvements, versioning, and reuse across UDFs or procedures. However, the JAR is not automatically deleted when the UDF is dropped—you must remove it manually. Also, TARGET_PATH will fail if the file already exists at that location.

Here's some code showing how we'd create a UDF using the TARGET_PATH parameter::

- CREATE OR REPLACE FUNCTION add_one(x INT)
- RETURNS INT
- LANGUAGE JAVA
- RUNTIME_VERSION = '11'
- HANDLER = 'MyClass.addOne'
- TARGET_PATH = '@handlers/add_one.jar'
- AS $$
- class MyClass {
- public static int addOne(int x) {
- return x + 1;
- }
- }
- $$;

To clean up after dropping the function:

- DROP FUNCTION add_one(INT);
- REMOVE @handlers/add_one.jar;

  

  

Question 75

Incorrect

What is one key benefit of **sensitive data classification** for data governance?

Choose **one** correct answer.

  

It use machine learning to classify column automatically into PII and non-PII

Explanation

While Snowflake supports automatic classification, it doesn’t rely on machine learning by default, and classification tagging is a multi-step process—automatic tagging is optional.

**Correct answer**

  

Columns can be marked as having sensitive or PII data

Explanation

This classification process attaches Snowflake system tags to columns, enabling identification and consistent governance of sensitive or personally identifiable information (PII) throughout the data lifecycle.

**Your answer is incorrect**

  

Columns are marked as having sensitive or PII data which automatically masks them

Explanation

Classification only applies tags to columns; applying masking or row-access policies requires separate action.

  

Overall explanation

Sensitive data classification in Snowflake helps you keep track of where important or private data, like email addresses or national insurance numbers, lives in your tables. You can tag columns directly in Snowflake to say, “this one contains PII” or “this is a credit card number.” These tags don’t change the data, but they make it much easier to find and manage sensitive information across your database.

For example, if you have a customers table and you want to mark the email column as containing personal information, you can run:

- ALTER TABLE customers 
- MODIFY COLUMN email 
- SET TAG SYSTEM$PRIVACY_CATEGORY = 'PII',
- SYSTEM$SEMANTIC_CATEGORY = 'EMAIL_ADDRESS';

Now that column is clearly labelled, and you (or anyone managing security or compliance) can search for all columns with the 'PII' tag using a system view:

- sql
- CopyEditSELECT * 
- FROM SNOWFLAKE.INFORMATION_SCHEMA.TAG_REFERENCES
- WHERE TAG_NAME = 'PRIVACY_CATEGORY' AND TAG_VALUE = 'PII';

This makes it way easier to build reports, apply masking rules, or prove to auditors that you know where your sensitive data is. It’s a practical, low-friction way to get better visibility into the data that needs protecting.

  

**Question 83**

Incorrect

If a directory table is enabled on a stage object, which additional field is displayed when compared to the output of the LIST command?

Choose **one** correct answer.

  

Last modified time

Explanation

This metadata is included in both the LIST command and directory tables.

**Correct answer**

  

File URL

Explanation

The FILE_URL column, which provides a secure Snowflake-generated link to access the staged file, is available only through directory tables—not through the LIST command.

**Your answer is incorrect**

  

File hash

Explanation

MD5 hash column is included in both the LIST command and directory tables.

  

File size

Explanation

File size is shown in both LIST command output and directory table queries.

Overall explanation

In Snowflake, enabling a **directory table** on an internal stage provides a more detailed queryable interface for retrieving metadata about staged files. While the LIST command returns basic information like file name, size, and last modified time, querying a directory table reveals additional fields such as:

- FILE_URL – A pre-signed Snowflake-hosted URL that allows secure access to the staged file.  
    
- RELATIVE_PATH – The path to the file relative to the stage root.  
    
- MD5, ETAG – Checksum and ETag identifiers for integrity validation.  
    

This makes directory tables especially useful for managing unstructured data (e.g., PDFs, images, CSVs) and building pipelines or views that link file metadata with structured Snowflake tables.

Here's an example of querying a directory table:

- SELECT FILE_URL 
- FROM DIRECTORY(@mystage) 
- WHERE RELATIVE_PATH LIKE '%.csv';

  

**Question 96**

Incorrect

Which metadata columns are returned when reading a stream?

Choose **three** correct answers.

**Correct selection**

  

METADATA$ACTION

Explanation

This tells you whether a row was inserted or deleted, helping you understand what kind of change occurred.

  

METADATA$STATUS

Explanation

There is no metadata column called METADATA$STATUS in Snowflake streams.

**Your selection is incorrect**

  

METADATA$TIMESTAMP

Explanation

There is no metadata column called METADATA$TIMESTAMP in Snowflake streams.

**Your selection is correct**

  

METADATA$ROW_ID

Explanation

This column provides a unique and stable ID for the row, useful for tracking changes over time.

**Your selection is correct**

  

METADATA$ISUPDATE

Explanation

This column flags whether the current insert or delete is part of an update operation.

  

  

**Question 97**

Incorrect

What is the primary difference between the URLs generated by BUILD_SCOPED_FILE_URL and GET_PRESIGNED_URL?

Choose **one** correct answer.

**Your answer is incorrect**

  

BUILD_SCOPED_FILE_URL creates permanent URLs

Explanation

The URLs generated by BUILD_SCOPED_FILE_URL are temporary and expire after 24 hours. They are not permanent.

  

GET_PRESIGNED_URL supports encryption

Explanation

Both functions can be used with encrypted files. Encryption support is not the primary distinction between them.

**Correct answer**

  

GET_PRESIGNED_URL needs an expiration time

  

Overall explanation

Snowflake provides multiple file access functions for working with staged files. Two of these functions—BUILD_SCOPED_FILE_URL and GET_PRESIGNED_URL—generate URLs that allow secure access to files, but they behave differently:

- GET_PRESIGNED_URL is used with external stages (e.g., S3, Azure, GCS) and requires an expiration time to define how long the link will remain valid. It generates a temporary, signed URL that allows external access to the file.  
    
- BUILD_SCOPED_FILE_URL is used primarily with internal stages and returns a scoped file URL that is valid for 24 hours by default. You don’t need to explicitly specify an expiration time.  
    

Here's some code examples showing the calling of these two functions:

- -- Presigned URL for external stage file (requires expiration)
- SELECT GET_PRESIGNED_URL(@my_ext_stage, 'data/report.csv', 3600);

- -- Scoped URL for internal stage file (valid 24 hours)
- SELECT BUILD_SCOPED_FILE_URL(@my_stage, 'logs/log1.txt');

  

  

**Question 98**

Incorrect

Which of the following are characteristics of Snowflake’s Virtual Warehouses?

Choose **two** correct answers.

**Correct selection**

  

They are isolated from one another to avoid resource contention

Explanation

Each virtual warehouse operates independently, ensuring that workloads do not interfere with each other, preventing resource contention.

  

They store raw data permanently

Explanation

Virtual warehouses do not store data permanently; they are compute resources. Data storage is handled separately in Snowflake's centralised storage layer.

  

They support eventual consistency for data synchronization

Explanation

Snowflake provides immediate consistency, not eventual consistency, ensuring that all users see the same data at the same time.

**Your selection is correct**

  

They can be resized at any time

  

  

Overall explanation

Snowflake’s virtual warehouses are independent compute clusters that handle query processing and DML operations. One of their key strengths is **dynamic scalability** — warehouses can be resized at any time, even while running, to adapt to changing performance needs. This means you can start with a small warehouse for light queries and scale up to a larger size for heavier workloads, helping balance performance and cost.

Another core characteristic is **complete isolation** between warehouses. Each virtual warehouse runs independently, even if multiple warehouses are querying the same data. This design ensures there's no resource contention — heavy workloads on one warehouse won't degrade the performance of others. For example, an ELT pipeline can run in one warehouse, while analysts query dashboards in another, with no interference.

These two capabilities — on-demand scalability and isolation — are central to Snowflake’s elastic architecture, making it easier to support multiple teams, concurrent workloads, and variable demand without performance bottlenecks.

  

**Question 99**

Incorrect

Which privilege does a role need to set a data masking policy on a column?

Choose **one** correct answer.

  

SET

Explanation

There is no SET data masking policy privilege in Snowflake.

  

USAGE

Explanation

The USAGE privilege is not appropriate in this circumstance. USAGE is not required to set a masking possibly on a column.

**Correct answer**

  

APPLY

Explanation

The APPLY MASKING POLICY global privilege is the correct privilege needed to set a data masking policy on a column. This privilege allows a role to apply specific data masking rules or policies to columns in a database table, ensuring sensitive data is protected:

- ALTER TABLE IF EXISTS employee MODIFY COLUMN email
- SET MASKING POLICY email_mask;

  

  

**Exam - 2**

  

**Question 15**

Incorrect

Which virtual warehouse setting can be adjusted to optimize warehouse cache utilization when running frequent and similar queries?

Choose **one** correct answer.

  

MIN_CLUSTER_COUNT

Explanation

MIN_CLUSTER_COUNT adjusts the number of compute clusters in a multi-cluster warehouse but does not directly impact caching.

**Correct answer**

  

AUTO_SUSPEND

Explanation

AUTO_SUSPEND controls how long a warehouse remains active before suspending; a longer auto-suspend time prevents cache from being cleared between queries, improving performance for frequent, similar queries.

  

  

**Question 22**

Incorrect

Which optional warehouse property in the CREATE WAREHOUSE command defines the policy for automatically starting and shutting down clusters in a multi-cluster warehouse?

Choose **one** correct answer.

**Correct answer**

  

SCALING_POLICY

Explanation

Controls how clusters in a multi-cluster warehouse start and stop.

- STANDARD: Adds clusters quickly to reduce queuing.  
    
- ECONOMY: Saves credits by fully using active clusters before adding more.  
    

  

**Question 23**

Incorrect

Which Snowflake driver allows users to run asynchronous queries with JavaScript for web development?

Choose **one** correct answer.

**Correct answer**

  

Node.js Driver

Explanation

The Node.js Driver is designed for JavaScript environments and allows developers to run asynchronous queries using callbacks or promises.

**Your answer is incorrect**

  

JDBC Driver

Explanation

The JDBC driver is intended for Java applications and does not support JavaScript or async operations.

  

Overall explanation

For JavaScript developers building web applications, the Snowflake Node.js Driver is the only option that supports native asynchronous queries. This capability is essential for handling non-blocking operations in JavaScript applications, especially in frameworks like Express or Next.js.

For example, use of the driver from the Snowflake documentation:

const connection = snowflake.createConnection({

account: 'my_account',

authenticator: 'oauth',

token: '<your-oauth-access-token>',

warehouse: 'COMPUTE_WH',

database: 'MY_DB',

schema: 'PUBLIC'

});

connection.connect((err, conn) => {

if (err) {

console.error('Unable to connect:', err.message);

} else {

conn.execute({

sqlText: 'SELECT CURRENT_USER()',

complete: (err, stmt, rows) => {

if (err) {

console.error('Failed to execute query:', err.message);

} else {

console.log('Query Result:', rows);

}

}

});

}

});

Other Snowflake drivers like JDBC (Java), ODBC (generic DB tools), or the Python Connector are built for their respective languages and do not provide the JavaScript async support needed for web apps.

  

  

**Question 25**

Incorrect

How long is Snowpipe's load history stored in metadata?

Choose **one** correct answer.

**Your answer is incorrect**

  

7 days

Explanation

Snowpipe metadata is stored longer than one week.

**Correct answer**

  

14 days

  

**Overall explanation**

**Snowpipe’s metadata includes key details like which files were ingested, when they were loaded, and any errors that occurred. This information is essential for troubleshooting and auditing data ingestion activities. Snowflake retains this metadata for 14 days by default.**

**You can access it using:**

- SELECT * 
- FROM TABLE(INFORMATION_SCHEMA.LOAD_HISTORY(
- PIPE_NAME => 'my_pipe',
- START_TIME => DATEADD(DAY, -14, CURRENT_TIMESTAMP())
- ));

**Alternatively, use this to check current pipe status:**

- SELECT SYSTEM$PIPE_STATUS('my_pipe');

**If you need longer tracking, it’s best to log ingestion data to a custom table or monitoring tool.**

  

  

**Question 26**

Incorrect

If an account creates and shares a personalized listing on the Snowflake Private Data Exchange, what type of account is it?

Choose **one** correct answer.

  

Supplier

Explanation

“Supplier” is not a Snowflake-defined term for this role; Snowflake uses “Provider” instead.

**Correct answer**

  

Provider

Explanation

A Provider is an account that creates and shares listings—including personalized ones—on a Snowflake Data Exchange. Providers define who can access the listing and manage its configuration.

  

Overall explanation

In Snowflake’s Data Exchange ecosystem, accounts fall into two main roles: Providers and Consumers. A Provider publishes listings—either free or personalized—to share datasets securely within a Private or Public Exchange. Personalized listings enable providers to invite specific consumers and replicate data on demand.

On the other hand, Consumers browse and subscribe to these listings to consume data. They do not have the authority to publish or configure shared datasets. Reader accounts are a special case: they allow data access without a full Snowflake login but still cannot create listings.

This provider-consumer relationship forms the backbone of secure, managed data sharing in Snowflake—especially within controlled environments like private exchanges and VPS deployments.

  

  

Question 40

Incorrect

Which statement about Snowflake's micro-partitions is accurate?

Choose **one** correct answer.

  

They can be resized dynamically after creation

Explanation

Snowflake does not allow resizing of micro-partitions after they are created. Their size and structure are determined at write-time and remain fixed. All modifications are handled through the creation of new micro-partitions.

**Correct answer**

  

They are immutable once written

Explanation

In Snowflake, micro-partitions are **immutable** once created. This means that when data is updated or deleted, the original micro-partitions remain unchanged, and new micro-partitions are created to represent the updated data.

  

  

**Question 42**

Incorrect

For Snowflake's multi-cluster warehouses, which scaling mode automatically adjusts the number of clusters based on the current workload?

Choose **one** correct answer.

  

Maximized

Explanation

In Maximized mode, the number of clusters is fixed; Snowflake starts all clusters specified, providing maximum resources continuously, regardless of workload fluctuations.

**Correct answer**

  

Auto-scale

Explanation

In Auto-scale mode, Snowflake dynamically starts and stops clusters based on the current workload, scaling the number of clusters between the defined minimum and maximum to handle varying query loads efficiently.

  

**Question 43**

Incorrect

When logging into your Snowflake account with Multi-Factor Authentication (MFA) enabled, which methods can you use on your second-factor device to verify your identity?

Choose **two** correct answers.

**Your selection is correct**

  

Receive a push notification

Explanation

If Duo Push is enabled, a push notification is sent to your Duo Mobile application. Approving this notification allows you to log into Snowflake.

**Correct selection**

  

Receive a phone call

Explanation

You can select "Call Me" to receive login instructions via a phone call to your registered mobile device.

**Your selection is incorrect**

  

Receive an email

Explanation

Snowflake's MFA does not utilize email as a method for second-factor authentication.

  

Overall explanation

When Multi-Factor Authentication (MFA) is enabled in Snowflake, there are multiple options to verify an identity using a second-factor device. Here is the diagram from the Snowflake documentation summarising the login flow when MFA is enabled:

  

  

  

  

**Question 56**

Incorrect

What does Snowflake's Search Optimization Service create to improve query performance?

Choose **one** correct answer.

**Your answer is incorrect**

  

B-Tree Index

Explanation

Snowflake doesn’t use traditional B‑tree or relational-style indexes.

**Correct answer**

  

Search Access Path

  

Overall explanation

Once the Search Optimization Service is enabled on a table (or on specific columns), Snowflake spins up a background maintenance task that constructs the **search access path**. This structure maps column values (e.g. for varchar, variant, geography) to their corresponding micro-partitions. During query execution—such as WHERE id = 1234, LIKE '%foo%', or geography filters—Snowflake uses this metadata to prune entire partitions that don’t contain relevant data, avoiding full table scans.

The search access path supports:

- Equality (=) and IN filters  
    
- Substring searches (e.g. LIKE '%term%', regex)  
    
- Semi‑structured data (VARIANT / OBJECT / ARRAY) point lookups and substring filters  
    
- Geospatial queries via supported functions.  
    

It's good to know that maintaining the search access path metadata incurs both compute and storage overheah, and it's up to you to determine if the query performance improvements for selective workloads outweigh the cost.

  

  

  

**Question 59**

Incorrect

Which of the following details are **not accessible** to a non-owner role when using a secure UDF?

Choose **two** correct answers.

  

Return type

Explanation

The function’s return data type remains visible to all users, as it's essential for correctly calling the UDF.

**Your selection is correct**

  

Handler code

Explanation

The handler code (the SQL, JavaScript, Python, or Java code that performs the UDF's logic) is the primary thing a secure UDF is designed to hide. As the documentation states: "[Secure UDFs allow you to protect the intellectual property in your UDF code when sharing UDFs with other Snowflake accounts... The function’s definition remains hidden...](https://docs.snowflake.com/en/developer-guide/secure-udf-procedure)" The handler code is the definition.

**Your selection is incorrect**

  

Parameter types

Explanation

Input argument types are visible to ensure correct usage by consumers.

**Correct selection**

  

List of imports

Explanation

When creating a secure UDF IMPORTS is the parameter used to specify, "[The location (stage), path, and name of the file(s) to import. A file can be a JAR file or another type of file.](https://docs.snowflake.com/en/developer-guide/secure-udf-procedure)"

If you don’t see any import list when you execute DESCRIBE FUNCTION <function_name>(), this means you don't have the necessary privileges to access that secure view. It's important to obfuscate the import list as it might reference external libraries or other secure components, which could expose sensitive logic or dependencies.

  

Handler language

Explanation

Similar to parameter types and the return type, this information must be known for users to effectively utilize the UDF.

Overall explanation

When a UDF is marked as SECURE, Snowflake intentionally conceals the implementation logic and external dependencies (such as IMPORTS, handler code, packages, and handler name) from all non-owner roles (and even masks them in the owner’s query profile). This enforces protection of proprietary logic and supports safe sharing. Meanwhile, interface-level metadata—like return type, parameter types, handler language, nullability, and volatility—remains visible to facilitate proper use of the function.

  

  

**Question 63**

Incorrect

What is the function used to create an ARRAY in Snowflake?

Choose **one** correct answer.

**Your answer is incorrect**

  

OBJECT_CONSTRUCT

Explanation

[Creates an object (key-value pairs), not an array.](https://docs.snowflake.com/en/sql-reference/functions/object_construct)

**Correct answer**

  

ARRAY_CONSTRUCT

  

Overall explanation

The ARRAY_CONSTRUCT function in Snowflake is used to create a new ARRAY from a list of zero or more input expressions. These expressions can be literal values, column references, or other valid Snowflake expressions that evaluate to a value. The function returns a new ARRAY containing the results of these expressions, in the order they are provided.

A common use case for ARRAY_CONSTRUCT is to create an array of values to be used in a WHERE clause with the ARRAY_CONTAINS or IN predicate. For example, if you want to select rows where a column named category is one of several specific values, you could use:

- SELECT *
- FROM products
- WHERE ARRAY_CONTAINS('Electronics'::VARIANT, ARRAY_CONSTRUCT('Electronics', 'Appliances', 'Books'));

- -- Or, more concisely with IN:
- SELECT * FROM products where category IN ('Electronics','Appliances','Books');

  

Question 78

Incorrect

In Snowflake stored procedures, which built-in exception is raised when an error occurs during the execution of a SQL statement, such as attempting to drop a non-existent table?

Choose **one** correct answer.

**Correct answer**

  

STATEMENT_ERROR

Explanation

STATEMENT_ERROR is the built-in exception that Snowflake raises when a SQL statement encounters an issue during execution. For example, attempting to drop a non-existent table would trigger this exception.

  

  

Overall explanation

when writing Snowflake stored procedures using SQL scripting, you can handle exceptions in an EXCEPTION block. Built-in exceptions include:

- **STATEMENT_ERROR**: Triggered when a SQL DDL/DML statement fails (e.g., dropping a non-existent table).  
    
- **EXPRESSION_ERROR**: Occurs when an error in an expression (like type casting or arithmetic) happens.  
    
- **OTHER**: A fallback for uncaught exceptions.  
    

By catching specific errors using these exceptions, you can make your procedures robust, provide custom error handling, or log detailed diagnostics using built-in variables like SQLCODE, SQLERRM, and SQLSTATE.

  

  

Question 79

Incorrect

In Snowflake, what is the outcome of specifying a seed value when performing fixed-size sampling using the SAMPLE clause?

Choose **one** correct answer.

**Your answer is incorrect**

  

The query will return a deterministic fixed-size sample based on the specified seed

Explanation

Snowflake does not support using a seed with fixed-size sampling; attempting to do so will result in an error.

  

The query will execute successfully, but the seed will be ignored, resulting in a non-deterministic sample

Explanation

Including a seed with fixed-size sampling is not supported in Snowflake and will cause the query to fail.

**Correct answer**

  

The query will fail with an error indicating that seeds are not supported for fixed-size sampling

Explanation

Snowflake does not allow the use of seeds with fixed-size sampling. Attempting to include a seed in such a query will result in an error.

  

The query will return a random sample of the specified size without considering the seed

Explanation

While fixed-size sampling returns a sample of the specified size, including a seed is not supported and will cause the query to fail.

Overall explanation

The SAMPLE clause in Snowflake offers two modes:

1. **Fraction-based sampling** (BERNOULLI or SYSTEM) with SEED, which allows reproducible results:

- SELECT * FROM my_table
- SAMPLE BERNOULLI (10) SEED (42);

3.   
      
      
    
4. **Fixed-size sampling** (e.g., SAMPLE (10 ROWS)), which returns a set number of rows but **does not support** SEED or REPEATABLE. Including them produces a syntax error:

- ERROR: Syntax error line x at position y unexpected 'SEED'.

6.   
      
      
    

If you need deterministic behavior with fixed-size sampling, you must get creative—such as using ROW_NUMBER() combined with HASH() and filtering based on a hash seed.

  

  

**Question 87**

Incorrect

Which of the following parameters is optional when using the GET_PRESIGNED_URL function in Snowflake?

Choose **one** correct answer.

  

Stage name

Explanation

The stage name is a required parameter that specifies the internal or external stage where the file is stored. 

**Your answer is incorrect**

  

Relative file path

Explanation

The relative file path is a required parameter that defines the path and filename of the file relative to its location on the stage. 

**Correct answer**

  

Expiration time

Explanation

The expiration time is an optional parameter that determines the length of time (in seconds) after which the pre-signed URL expires. If not specified, it defaults to 3600 seconds (60 minutes).

  

File size

Explanation

The GET_PRESIGNED_URL function does not require or accept a file size parameter.

Overall explanation

The GET_PRESIGNED_URL function returns a URL granting temporary access to a staged file without requiring Snowflake authentication. Its signature is:

GET_PRESIGNED_URL(@<stage_name>, '<relative_file_path>', [expiration_time])

<stage_name> and <relative_file_path> are required.  

[expiration_time] is optional, defaults to 3600 seconds, and its maximum is 3600s for AWS IAM roles or 604,800s for other setups.  

Use this feature to securely share files from Snowflake stages—especially useful within secure views or APIs where you need temporary access without credentials.

  

  

Question 88

Incorrect

Which HTTP method does the Snowflake File Support REST API provide to download files from stages?

Choose **one** correct answer.

**Your answer is incorrect**

  

POST

Explanation

The POST method is typically used to submit data to a server to create or update resources. In the context of the Snowflake File Support REST API, POST is not used for downloading files from stages.

**Correct answer**

  

GET

Explanation

The GET method is used to retrieve data from a server. In the Snowflake File Support REST API, the GET /api/files/ endpoint is specifically designed to download files from internal or external stages.

  

PUT

Explanation

The PUT method is generally used to upload or replace resources on a server. It is not used for downloading files in the Snowflake File Support REST API.

  

DELETE

Explanation

The DELETE method is used to remove resources from a server. It is not applicable for downloading files in the Snowflake File Support REST API.

Overall explanation

To download a file via Snowflake’s File Support REST API:

1. Generate a **scoped** or **file URL** using BUILD_SCOPED_FILE_URL, BUILD_STAGE_FILE_URL, or GET_PRESIGNED_URL.  
    
2. Send an **HTTP GET** request to the /api/files/ endpoint, including appropriate OAuth authorization.  
    
3. Snowflake responds with the file content, enabling external systems or clients to securely fetch staged data.  
    

  

**Question 96**

Incorrect

A Snowflake multi-cluster warehouse currently experiences query queuing during peak load times. Its current SCALING_POLICY is 'STANDARD', but MIN_CLUSTER_COUNT and MAX_CLUSTER_COUNT are at their default setting of 1. Which ALTER WAREHOUSE configuration best reduces queuing **cost-consciously**?

Choose **one** correct answer.

  

MAX_CLUSTER_COUNT = 10, SCALING_POLICY = 'ECONOMY', MIN_CLUSTER_COUNT = 1

Explanation

This configuration allows for high scaling but is likely excessive and might not be the _most_ cost-conscious, despite the 'ECONOMY' policy.

**Your answer is incorrect**

  

MAX_CLUSTER_COUNT = 5, SCALING_POLICY = 'STANDARD', MIN_CLUSTER_COUNT = 1

Explanation

This configuration provides more resources than the current setup, but 'STANDARD' scaling is more aggressive and thus more expensive.

**Correct answer**

  

MAX_CLUSTER_COUNT = 5, SCALING_POLICY = 'ECONOMY', MIN_CLUSTER_COUNT = 2

Explanation

This configuration balances scaling potential with cost efficiency by using 'ECONOMY' scaling and ensuring at least two warehouses are always active.

  

**Exam - 3**

  

**Question 9**

Incorrect

Which of the following statements about the COPY INTO <table> command in Snowflake are correct?

Choose **two** correct answers.

**Correct selection**

  

The command requires data files to be staged before loading into a table

Explanation

The COPY INTO <table> command in Snowflake loads data from files that have been staged in locations such as named internal [stage objects](https://docs.snowflake.com/en/sql-reference/sql/create-stage), external stage objects, or external locations like Amazon S3, Google Cloud Storage, or Microsoft Azure.

  

Data files must have the same number and ordering of columns as the target table

Explanation

The COPY INTO <table> command supports column reordering, column omission, and data type casting during the load process, meaning the data files do not need to have the same number or ordering of columns as the target table.

**Your selection is incorrect**

  

The command can load data directly from local files without staging

Explanation

Snowflake's COPY INTO <table> command requires data files to be staged before loading, either internally within Snowflake or in an external cloud storage location. It does not support loading data directly from local files such as those on your work or home desktop without staging.

**Your selection is correct**

  

The ON_ERROR option specifies the action to perform when errors are encountered during loading

Explanation

The ON_ERROR copy option in the COPY INTO <table> command determines the action to take if errors are encountered during the data loading process, such as continuing, skipping the file, or aborting the statement.

  

  

**Question 13**

Incorrect

Which of the following statements are true regarding Snowflake's warehouse cache?

Choose **two** correct answers.

**Your selection is incorrect**

  

The warehouse cache and the persisted query results cache are the same thing, both storing the results of completed queries

Explanation

The warehouse cache stores raw table data, while the persisted query results cache stores query results.

**Your selection is correct**

  

Query performance can improve if data is read from the warehouse cache instead of remote storage

Explanation

Snowflake stores table data in the warehouse cache when queries are executed. If a subsequent query accesses the same data, the warehouse can read from the cache instead of retrieving data from remote storage, significantly improving query performance.

  

The warehouse cache stores query results for reuse across different warehouses

Explanation

Each warehouse has its own cache, and cache is not shared across different warehouses. If queries are executed on a different warehouse, that warehouse must load the data from storage rather than using the cache from another warehouse.

**Correct selection**

  

The cache is automatically cleared when the warehouse is suspended

Explanation

When a warehouse is suspended, its cache is dropped. This means that after resuming, queries must fetch data from remote storage again, potentially slowing execution times. To maintain performance, users should adjust auto-suspend settings based on workload needs.

  

The warehouse cache eliminates the need for data retrieval from remote storage for all queries

Explanation

While warehouse cache can speed up queries, it does not eliminate data retrieval from storage in all cases. If a query requests new or uncached data, Snowflake must fetch it from storage.

Overall explanation

Snowflake succinctly summarises the warehouse cache in the following way: "[A running warehouse maintains a cache of table data that can be accessed by queries running on the same warehouse. This can improve the performance of subsequent queries if they are able to read from the cache instead of from tables.](https://docs.snowflake.com/en/user-guide/performance-query-warehouse-cache)"

However, the warehouse cache is cleared when a warehouse is suspended, meaning queries executed after resumption must reload data. To balance performance and cost, users should configure auto-suspend settings carefully—longer suspension times can help retain cache but at the cost of keeping the warehouse active and consuming credits.

  

**Question 21**

Incorrect

When creating a pipe object in Snowflake, which of the following parameters are optional?

Choose **two** correct answers.

**Correct selection**

  

ERROR_INTEGRATION

Explanation

This parameter is only required when configuring error notifications for a cloud messaging service. If no error notifications are needed, this parameter is optional.

**Your selection is incorrect**

  

FILE_FORMAT

Explanation

FILE_FORMAT is an optional parameter but not for the pipe object. It's an optional parameter for the COPY INTO <table> statement embedded in the pipe object.

  

COPY INTO <table> statement

Explanation

The copy statement is a required parameter when creating a pipe object. As the Snowflake documentation states, "[COPY INTO <table> statement used to load data from queued files into a Snowflake table. This statement serves as the text/definition for the pipe and is displayed in the SHOW PIPES output.](https://docs.snowflake.com/en/sql-reference/sql/create-pipe)"

**Your selection is correct**

  

AWS_SNS_TOPIC

Explanation

This parameter specifies the Amazon Resource Name (ARN) for an Amazon SNS topic for event notifications and is optional when creating a pipe. As the Snowflake documentation states, "[Specifies the Amazon Resource Name (ARN) for the SNS topic for your S3 bucket. The CREATE PIPE statement subscribes the Amazon Simple Queue Service (SQS) queue to the specified SNS topic. The pipe copies files to the ingest queue triggered by event notifications via the SNS topic. For more information, see Automating Snowpipe for Amazon S3.](https://docs.snowflake.com/en/sql-reference/sql/create-pipe)"

  

Pipe Identifier

Explanation

An identifier for the pipe object must always be supplied when creating a new pipe object.

Overall explanation

When creating a pipe in Snowflake, certain parameters are mandatory, while others are optional. The COPY INTO <table> statement and the pipe name are essential components that define the pipe's functionality and identity, making them required.

In contrast, parameters like ERROR_INTEGRATION, INTEGRATION, and AWS_SNS_TOPIC provide additional configurations and integrations but are optional, allowing flexibility based on specific use cases.

  

  

**Question 22**

Incorrect

To optimise performance and cost when using Snowpipe, how frequently does Snowflake recommend staging data files?

Choose **one** correct answer.

  

Less than 1 file per minute

Explanation

While Snowpipe can handle less frequent file arrivals, this is often less efficient. Snowpipe's pricing is based on resource consumption, and very infrequent, small files can lead to higher relative overhead.

**Correct answer**

  

Around 1 file per minute

Explanation

This is the sweet spot recommended by Snowflake. It allows Snowpipe to efficiently utilize resources and provides a good balance between latency (how quickly data is loaded) and cost. This allows the files to be grouped into a reasonable size for processing.

  

**General file sizing recommendations**

The number of load operations that run in parallel can’t exceed the number of data files to be loaded. To optimize the number of parallel operations for a load, we recommend aiming to produce data files roughly 100-250 MB (or larger) in size **_compressed_**.

  

**Size limits for database objects**

When you use any of the available methods for [loading data into Snowflake](https://docs.snowflake.com/en/user-guide/data-load-overview), you can store objects with sizes up to the following limits:

|   |   |
|---|---|
|**Data type**|**Storage limit**|
|ARRAY|128 MB|
|BINARY|64 MB|
|GEOGRAPHY|64 MB|
|GEOMETRY|64 MB|
|OBJECT|128 MB|
|VARCHAR|128 MB|
|VARIANT|128 MB|

  

  

  

  

**Question 23**

Incorrect

In Snowflake's Data Exchange, which party is primarily responsible for configuring the exchange and managing its members?

Choose **one** correct answer.

**Your answer is incorrect**

  

Data Provider 

Explanation

A Data Provider publishes data to the exchange for consumers to access but does not have the authority to configure the exchange or manage its members.

  

Data Consumer 

Explanation

A Data Consumer accesses and utilizes data available in the exchange but does not have administrative responsibilities over the exchange's configuration or membership.

**Correct answer**

  

Data Exchange Administrator 

Explanation

The Data Exchange Administrator is responsible for configuring the Data Exchange and managing its members, including adding or removing members and designating roles such as providers or consumers.

  

Overall explanation

Snowflake Data Exchange is a secure, controlled environment where organizations can privately share data between accounts without the need for complex ETL pipelines. It allows data providers to publish datasets and data consumers to access them in real-time while maintaining governance and security.

  

  

  

The diagram above illustrates a Data Exchange where an organization is publishing and accessing datasets shared between internal accounts as well as external organisations.

'Your Organization' on the left consists of a Snowflake account and an external Reader/Writer Account (Company A). These accounts share data to a Data Exchange where listings (datasets) are published. If you want to get a sense of how you create and publish a data listing to an exchange, check out this [documentation page](https://docs.snowflake.com/en/user-guide/data-exchange-managing-data-listings#create-and-publish-a-data-listing). Other organisations, such as Company B, can then access and publish their datasets through the same exchange.

The **Data Exchange Administrator** plays a key role in managing this environment, they configure the Data Exchange to control access and data-sharing policies, they add or remove members like Company A and Company B and they also ensure secure data sharing without duplicating datasets.

  

  

**Question 30**

Incorrect

A data analyst is comparing two customer datasets in Snowflake, ecommerce_customers and retail_customers, to estimate how similar their customer_id values are. To avoid computing expensive set operations such as intersections or unions, which SQL statement would most efficiently estimate their similarity?

Choose **one** correct answer.

  

- SELECT APPROXIMATE_SIMILARITY(MINHASH(100, customer_id)) 
- FROM ecommerce_customers 
- JOIN retail_customers USING (customer_id);

Explanation

This joins the two tables and applies MinHash to only the overlapping customer_ids. It doesn’t compare the full sets independently, which is required for an unbiased similarity estimate.

**Correct answer**

  

- SELECT APPROXIMATE_SIMILARITY(mh) FROM (
- (SELECT MINHASH(100, customer_id) AS mh FROM ecommerce_customers)
- UNION ALL
- (SELECT MINHASH(100, customer_id) FROM retail_customers)
- );

Explanation

This is the correct and recommended pattern from Snowflake documentation for estimating set similarity using MinHash. It independently generates MinHash states from both input sets and combines them with UNION ALL, then passes the combined column to APPROXIMATE_SIMILARITY.

  

Question 34

Incorrect

A data engineer needs to generate a unique identifier for each row in a Snowflake table. Which type of function should be used?

Choose **one** correct answer.

  

Aggregate

Explanation

Aggregate functions summarize multiple rows into a single result (e.g., SUM(), MAX()), which is not suitable for generating row-level unique values.

  

Table

Explanation

Table functions return multiple rows and are often used for complex data generation or transformation across sets of rows, not for per-row identifiers.

**Correct answer**

  

Scalar

Explanation

Scalar functions return one value per input row, making them ideal for generating unique values per row. For example, UUID_STRING() is a scalar function that can assign a unique identifier to each transaction.

**Your answer is incorrect**

  

System

Explanation

System functions are used for administrative tasks like monitoring or managing the Snowflake system, not for generating row-level data.

Overall explanation

Scalar functions in Snowflake operate on individual rows and return a single result per row, making them ideal for row-level operations like generating unique identifiers. For instance, using UUID_STRING() allows users to tag each row with a unique value. This differs from aggregate functions, which are used for summarizing multiple rows, or system functions, which perform administrative tasks.

  

**Question 39**

Incorrect

Which SnowSQL connection property is used to supply an MFA-generated passcode during authentication?

Choose **one** correct answer.

  

--passcode

Explanation

There is no --passcode connection property in SnowSQL.

  

--mfa-token

Explanation

SnowSQL does not recognize --mfa-token as a valid connection property for supplying MFA passcodes.

**Correct answer**

  

--mfa-passcode

Explanation

The --mfa-passcode connection property in SnowSQL allows users to provide a multi-factor authentication (MFA) passcode directly during the authentication process. This is particularly useful when users prefer to enter a passcode instead of using the default Duo Push notification.

  

**Question 40**

Incorrect

Which command correctly creates a network rule object to block all public IPv4 access to your Snowflake account?

Choose **one** correct answer.

**Correct answer**

  

CREATE NETWORK RULE block_public_access 

MODE = INGRESS 

TYPE = IPV4 

VALUE_LIST = ('0.0.0.0/0');

Explanation

This is the correct syntax to create a Snowflake network rule object that blocks all incoming public IPv4 traffic to your account by specifying '0.0.0.0/0', representing all possible IPv4 addresses.

  

Question 51

Incorrect

Which function should be used inside a row access policy to check if a specific role (for example, ANALYST_ROLE) is currently active in the user’s session?

Choose **one** correct answer.

**Your answer is incorrect**

  

**CURRENT_ROLE**

Explanation

This returns only the primary role of the user’s session. It would not detect if ANALYST_ROLE is active as a secondary role unless it happens to be the primary. For comprehensive role checks, Snowflake suggests not relying solely on CURRENT_ROLE when multiple roles might be active .

  

CURRENT_SECONDARY_ROLES

Explanation

This function provides the set of secondary roles in JSON format . There is no direct boolean result, so using it in a policy would require parsing the JSON to find a role, which is cumbersome and not the intended use in policy conditions.

**Correct answer**

  

IS_ROLE_IN_SESSION

Explanation

This is exactly the purpose of IS_ROLE_IN_SESSION: to return TRUE if a given role (e.g. ANALYST_ROLE) is among the active roles for the current user’s session. Snowflake explicitly recommends this function for row access policies when checking a role’s presence in the session.

  

Overall explanation

Snowflake provides context functions that can be used in row access policy expressions to determine session attributes like the current user or roles. To check if a certain role is active in the user’s session (meaning it could be either the primary role or one of the secondary roles the user has enabled), the appropriate function is IS_ROLE_IN_SESSION('ROLE_NAME').

This function returns a Boolean indicating whether the specified role is among the currently active roles in the session. The official documentation recommends using IS_ROLE_IN_SESSION in policy conditions when role-based access logic is needed and especially if a role hierarchy or multiple active roles are involved . In other words, IS_ROLE_IN_SESSION('ANALYST_ROLE') will yield TRUE if the user has ANALYST_ROLE active, even if it’s a secondary role, which is exactly what the row access policy needs to know in this scenario.

  

  

Question 59

Incorrect

You have a JSON file staged in Snowflake with data like this:

{

"user": {

"id": "abc123",

"signup_date": "2024-01-15"

},

"event": "login"

}

You want to store user.id, user.signup_date, and event as separate columns in a structured table. Which approach should you use?

Choose **one** correct answer.

  

Load the entire file into a STRING column and parse it manually later

Explanation

This would not map the fields of the JSON file to a table columns. Downstream you'd have to parse the columns from the single STRING column. It's important to note this would also lack native semi-structured type support, like parsing the data with semi-structured functions.

  

Load into a VARIANT column and always query with dot notation

Explanation

Keeping everything in VARIANT is flexible but doesn’t create structured columns.

**Correct answer**

  

Use SQL to extract each field and insert into separate typed columns during load

Explanation

This is the ETL-style approach: extract values from the nested JSON and insert them into individual columns (e.g., data:user.id::STRING)

**Your answer is incorrect**

  

Use FLATTEN to automatically convert all nested fields into columns

Explanation

FLATTEN is used to explode arrays, not to extract structured fields into columns

Let me know if you’d like a companion code snippet to show how this looks in practice!

Overall explanation

When working with hierarchical semi-structured data (like JSON), one common technique in Snowflake is to explicitly extract fields from the raw data and insert them into separate, typed columns in a structured table. This is known as an ETL-style approach:  
Extract → Transform → Load.

This method is ideal when:

- You know the structure of the incoming data  
    
- You want to optimize performance (e.g., for pruning or compression)  
    
- You want native Snowflake data types like DATE, STRING, or NUMBER for analytics  
    

Let’s say you have the JSON files staged in @my_stage:

{

"user": {

"id": "abc123",

"signup_date": "2024-01-15"

},

"event": "login"

}

Here’s how you would extract and load that data into a structured table:

-- Step 1: Create a target table with typed columns

CREATE OR REPLACE TABLE user_events (

user_id STRING,

signup_date DATE,

event_type STRING

);

-- Step 2: Load the staged JSON file and extract fields

COPY INTO user_events

FROM (

SELECT

$1:user.id::STRING,

$1:user.signup_date::DATE,

$1:event::STRING

FROM @my_stage

)

FILE_FORMAT = (TYPE = 'JSON');

  

**Question 66**

Incorrect

What is the maximum number of rows that can be inserted using the VALUES clause in a single INSERT statement in Snowflake?

Choose **one** correct answer.

  

1048576

Explanation

This is not a defined limit for the VALUES clause in Snowflake.

**Your answer is incorrect**

  

100000

Explanation

While some systems may allow this many rows in one insert, Snowflake imposes a stricter limit.

**Correct answer**

  

16384

  

**Question 89**

Incorrect

Which two of the following statements about Streamlit apps in Snowflake are correct?

Choose **two** correct answers.

**Your selection is correct**

  

A Streamlit app in Snowflake runs using the privileges of the role that owns (created) the app

Explanation

Streamlit apps execute with the privileges of their **owner’s role**, not the viewer’s. In Snowflake’s “owner’s rights” model, the app runs as if the owner is performing the actions.

  

A Streamlit app uses the current user’s active database and schema when running

Explanation

The app does not use the caller’s current database or schema context. Instead, it always operates in the database and schema where the Streamlit app object was created (the owner’s context) .

  

Cloning a schema that contains a Streamlit app will also clone the Streamlit app

Explanation

Streamlit app objects are not cloned when you clone a schema or database.

**Correct selection**

  

A Snowflake virtual warehouse is required to execute a Streamlit app

Explanation

A Streamlit app requires a Snowflake warehouse to run. All Streamlit in Snowflake apps execute on a designated virtual warehouse for both the app’s Python code and any SQL queries it runs .

  

  

Overall explanation

Snowflake’s integration of Streamlit uses Snowflake’s owner’s rights security model and Snowflake-managed compute. This means a deployed Streamlit app runs inside Snowflake with the privileges and resources of its owner, rather than the end user.

For example, if a Streamlit app is created by a role with access to a table with sensitive data, any user who can view the app will see the data from that table through the app – because the app executes with the app owner’s role privileges .

Similarly, the app runs on a Snowflake virtual warehouse chosen by the owner, not on the viewer’s machine. This secure-by-design model eliminates the need to expose data or code outside Snowflake’s environment

  

**Question 90**

Incorrect

What is the maximum size of data that can be exchanged in a single message between a Streamlit app’s backend and frontend in Snowflake?

Choose **one** correct answer.

  

16 MB

Explanation

16 MB is not the correct limit. The actual documented limit is higher than this.

**Correct answer**

  

32 MB

Explanation

32 MB is the correct maximum message size for Streamlit apps in Snowflake. Streamlit apps running in Snowflake (or as Native Apps) have a 32-MB limit on the size of messages exchanged between the backend (Python execution in Snowflake) and the frontend (the web interface)

**Your answer is incorrect**

  

64 MB

Explanation

64 MB is not the correct limit. The actual documented limit is lower than this.

  

No fixed limit (unlimited)

Explanation

There is a fixed limit; it’s not unlimited

Overall explanation

While Streamlit apps in Snowflake can query and display Snowflake data, there is a technical limit on how much data can be sent from the Snowflake backend to the app’s frontend in a single interaction. This is essentially a size limit on the messages exchanged between the app’s Python backend and the browser interface. If an app tries to fetch or transmit a very large result exceeding this size, Snowflake will not send it. Instead, the app will encounter an error indicating the message is too large. Knowing this limit is important so we can fetch data in smaller chunks or use other strategies for big data sets.

  

**Question 92**

Incorrect

An administrator is managing a virtual warehouse named WH_ETL that is currently running and consuming compute resources. To minimize costs after completing data processing tasks, which SQL command should they execute to stop the warehouse's operations without deleting it?

Choose **one** correct answer.

  

DROP WAREHOUSE WH_ETL;

Explanation

This command permanently deletes the warehouse, removing its configuration and history. It's not suitable when you intend to stop operations temporarily without losing the warehouse setup.

**Your answer is incorrect**

  

ALTER WAREHOUSE WH_ETL SET AUTO_SUSPEND = 0;

Explanation

Setting AUTO_SUSPEND to 0 disables the auto-suspend feature, meaning the warehouse will not suspend automatically due to inactivity. It does not immediately stop the warehouse.

**Correct answer**

  

ALTER WAREHOUSE WH_ETL SUSPEND;

  

**Question 93**

Incorrect

Which two of the following query patterns are typically eligible for acceleration by Snowflake's Query Acceleration Service (QAS)?

Choose **two** correct answers.

**Your selection is correct**

  

Large table scans that include a highly selective filter or an aggregation

Explanation

Large scans with a selective filter or with an aggregation benefit from QAS . These queries have sizable scan operations that QAS can offload and parallelise, making them good candidates for acceleration.

  

Queries that make use of nondeterministic functions like RANDOM()

Explanation

Queries using nondeterministic functions like RANDOM() or SEQ cannot be accelerated by QAS.

**Your selection is incorrect**

  

Queries containing a LIMIT clause without an ORDER BY clause

Explanation

QAS will not accelerate a query with a LIMIT but no ORDER BY.

**Correct selection**

  

Large data-loading queries that insert or copy a high volume of new rows

Explanation

Large data-loading operations (e.g., INSERT ... SELECT or COPY INTO for many rows) involve scanning large data and writing results, which are the types of operations QAS is intended to improve.

  

  

**Question 98**

Incorrect

What is the granularity of data in the ACCESS_HISTORY view in Snowflake?

Choose **one** correct answer.

  

One record per user session

Explanation

Access history is not session-based; multiple queries in a single session will each generate their own record.

  

One record per day

Explanation

The view includes timestamps for when queries were executed, but each row represents a specific query event, not a daily summary.

**Correct answer**

  

One record per query execution

Explanation

The ACCESS_HISTORY view provides one row for each query execution, allowing detailed tracking of which objects were accessed, by whom, and how.

  

**Question 99**

Incorrect

An analyst wants to analyze the execution plan of a previously run SQL query in **JSON** format. Which of the following statements will correctly return the JSON-formatted plan for their last executed query?

Choose **one** correct answer.

**Correct answer**

  

SELECT SYSTEM$EXPLAIN_PLAN_JSON(LAST_QUERY_ID());

Explanation

This is the correct syntax to get the JSON-formatted execution plan for a previously executed query using its query ID.

  

  

**Exam - 4**

  

**Question 1**

Incorrect

A user is assigned the DATA_ENGINEER role, which has the CREATE TABLE privilege. During a session, the user activates DATA_ENGINEER as a **secondary role**. Can the user create a table?

Choose **one** correct answer.

**Your answer is incorrect**

  

Yes, because the role is active in the session

Explanation

The role is active, but being a secondary role only enables SELECT/UPDATE/DELETE, not object creation.CREATE TABLE statements are authorized **only by the primary role**

**Correct answer**

  

No, because only the primary role grants CREATE TABLE privileges

Explanation

Object creation requires privileges from the **active primary role**. Even if the secondary role has CREATE TABLE privileges, it won’t apply unless it's the primary role.

  

Yes, as long as the role has the required privilege

Explanation

Having the privilege isn't sufficient; it must also be the **primary role** at runtime. Secondary roles can't authorize object creation, regardless of granted privileges.

  

No, because secondary roles do not authorise SQL operations

Explanation

Secondary roles can perform many operations, such as SELECT, UPDATE, or DELETE, depending on granted privileges.

Overall explanation

In Snowflake, user privileges are determined by the active roles during a session: a single primary role and any number of secondary roles. While secondary roles expand access for most SQL actions, they do not authorize object creation (e.g., CREATE TABLE, CREATE VIEW). Only the active primary role can authorize such actions and will be recorded as the object owner.

Here's how it looks if we break it down with a real example. A user has two roles:

- DATA_ENGINEER (granted CREATE TABLE)  
    
- ANALYST (granted SELECT)  
    

If ANALYST is set as the primary role and DATA_ENGINEER as a secondary, the user can query data but cannot create tables. To create tables, DATA_ENGINEER must be switched to the primary role using USE ROLE DATA_ENGINEER.

  

  

**Question 3**

Incorrect

Which function is used to extract a value from a VARIANT column containing semi-structured data by specifying a key or index?

Choose **one** correct answer.

  

Overall explanation

In Snowflake, the GET function is utilized to extract values from semi-structured data stored in VARIANT columns. When working with an OBJECT, you can specify a key to retrieve the corresponding value: SELECT src:get('key_name') FROM table_name;. For ARRAY data, you can use an index to access a specific element: SELECT src:get(0) FROM table_name;. If the specified key or index does not exist, the function returns NULL. This capability allows for precise extraction of elements within semi-structured data, facilitating more efficient data analysis and manipulation.

  

  

**Question 9**

Incorrect

Which parameter in Snowflake's COPY INTO <table> command allows loading files that match a specific regular expression?

Choose **one** correct answer.

**Your answer is incorrect**

  

FILES

Explanation

The FILES parameter specifies a list of specific file names to load from the stage. It does not support regular expressions but requires explicit file names.

**Correct answer**

  

PATTERN

Explanation

The PATTERN parameter allows the use of regular expressions to select files for loading based on their names. This enables flexible and dynamic file selection during the data load process.

  

Overall explanation

Here's a simple example showing the PATTERN parameter in action:

- COPY INTO my_table
- FROM @my_stage
- FILE_FORMAT = (TYPE = 'CSV')
- PATTERN = '.*sales.*\.csv';

In this example, the PATTERN parameter uses a regular expression to match file names containing 'sales' and ending with '.csv', this way we load only CSV files from the stage where the file names contain the word 'sales'.

Understanding the role of each parameter in the COPY INTO <table> command is essential for efficient and accurate data loading in Snowflake.

  

Question 10

Incorrect

Which of the following SQL statements in Snowflake utilize the metadata cache for optimized performance?

Select **two** correct answers.

**Your selection is correct**

  

SELECT COUNT(*) FROM orders;

Explanation

Snowflake stores row counts in its metadata cache, allowing this query to return results instantly without scanning the entire table.

**Correct selection**

  

SELECT CURRENT_DATABASE();

Explanation

Fetching the current session database is a metadata-only query, meaning Snowflake does not need to scan any data to return the result.

  

Overall explanation

Snowflake optimizes performance by caching table-level metadata such as:

- Row count (SELECT COUNT(*))  
    
- Table and session details (SELECT CURRENT_DATABASE())  
    
- Min/max values for numeric and date columns (but not strings)  
    

Other queries, including aggregations, sorting, and column-based functions, require actual data scans, making them ineligible for metadata caching.

By leveraging metadata cache-aware queries, users can execute lightweight, high-speed lookups in Snowflake.

  

Question 11

Incorrect

A data engineer needs to list all tables within a specific schema named my_schema in a database named my_database using the SHOW command, but they only want to see tables that have a name starting with the prefix "sales_". Which of the following commands will achieve this?

  

**Overall explanation**

**The SHOW <objects> command allows us to list all instances of a specific object type within a scope, such as a database or schema. Here's the generic syntax for the command:**

- SHOW OBJECTS [ LIKE '<pattern>' ]
- [ IN { ACCOUNT | DATABASE <database_name> | SCHEMA <schema_name> } ];
- LIKE '<pattern>' is optional and can filter objects by name.  
    
- IN clause is optional and specifies the scope (ACCOUNT, DATABASE, or SCHEMA)  
    

**Here's an example from the Snowflake documentation listing all the tables which have the word 'PART' in a schema called 'tpch_sf1':**

- SHOW TERSE TABLES LIKE '%PART%' IN tpch_sf1;

**Output:**

- +-------------------------------+-----------+-------+-----------------------+-------------+
- | created_on | name | kind | database_name | schema_name |
- |-------------------------------+-----------+-------+-----------------------+-------------|
- | 2016-07-08 13:41:59.960 -0700 | JPART | TABLE | SNOWFLAKE_SAMPLE_DATA | TPCH_SF1 |
- | 2016-07-08 13:41:59.960 -0700 | JPARTSUPP | TABLE | SNOWFLAKE_SAMPLE_DATA | TPCH_SF1 |
- | 2016-07-08 13:41:59.960 -0700 | PART | TABLE | SNOWFLAKE_SAMPLE_DATA | TPCH_SF1 |
- | 2016-07-08 13:41:59.960 -0700 | PARTSUPP | TABLE | SNOWFLAKE_SAMPLE_DATA | TPCH_SF1 |
- +-------------------------------+-----------+-------+-----------------------+-------------+

**The keyword TERSE is an optional parameter used to return only a subset of the available output columns.**

  

  

Question 13

Incorrect

You've just run a query in Snowflake and want to determine if it utilised the warehouse cache. Which statistic in the Snowsight Query Profile tool would give you the most direct indication of warehouse cache usage?

Choose **one** correct answer.

  

Bytes scanned

Explanation

This metric only reports the total amount of data scanned but does not indicate whether the data came from cache or remote storage.

  

Data scanned from cache

Explanation

This is not a valid metric in the Snowsight Query Profile tool. The correct metric is Percentage scanned from cache.

**Correct answer**

  

Percentage scanned from cache

Explanation

This metric shows what percentage of the total scanned data was retrieved from the warehouse cache instead of remote storage. A higher percentage means the query benefited significantly from cached data, improving performance and reducing storage I/O costs.

**Your answer is incorrect**

  

Bytes scanned from cache

Explanation

This is not a valid metric in the Snowsight Query Profile tool. The correct metric is Percentage scanned from cache.

Overall explanation

Snowflake’s warehouse cache (also referred to as the local disk cache) helps speed up queries by storing table data in memory and SSDs, allowing repeated queries to access cached data instead of remote storage. This reduces query execution time and lowers compute costs.

To determine if a query leveraged the warehouse cache, check the Snowsight Query Profile tool for the target query and look at 'Percentage scanned from cache' statistic in the panel on the right-hand side:

- A high percentage (e.g., 80-100%) means most of the data was retrieved from cache, improving performance.  
    
- A low percentage (e.g., <20%) suggests most data came from remote storage, meaning warehouse caching had minimal impact.  
    

Here's how it looks on the Query Profile itself with 100% of bytes scanned from the warehouse cache:

  

  

  

Question 14

Incorrect

When cloning a database or schema in Snowflake, which of the following objects are **not** included in the clone?

Choose **two** correct answers.

**Correct selection**

  

External tables

Explanation

These tables reference data stored outside of Snowflake, such as in external stages or cloud storage. When cloning a database or schema, external tables are not included in the clone because they point to data outside Snowflake's managed storage.

**Your selection is incorrect**

  

Hybrid tables 

Explanation

Hybrid tables combine features of standard and external tables. They can be cloned at the database level but not at the schema level. This means that if you clone a database containing hybrid tables, those tables will be included in the clone. However, cloning a schema that contains hybrid tables will not include those tables in the cloned schema.

  

Views

Explanation

Logical representations of stored queries. Views are included in the clone when a database or schema is cloned.

**Your selection is correct**

  

Internal (Snowflake) stages

Explanation

Internal stages are Snowflake-managed storage locations used for data loading and unloading. These stages are not cloned during database or schema cloning operations, meaning any data files in these stages are not copied to the clone.

  

Materialized views

Explanation

These are views that store the result set of a query physically. Materialized views are included in the clone when a database or schema is cloned.

Overall explanation

The key to understanding what objects are included and excluded when cloning a database or schema lies in differentiating between metadata and data. The clone includes all the metadata defining the objects within the database or schema. This includes:

- Tables: The table definitions (column names, data types, etc.) are cloned, and the clone initially points to the same micro-partitions as the original table.  
    
- Views: Views are logical objects (SQL queries), and their definitions are cloned.  
    
- User-Defined Functions (UDFs): The code and definitions of UDFs are cloned.  
    
- Sequences: The sequences and their current value and other properties are cloned.  
    
- Stored Procedures  
    
- File Formats  
    

However, certain objects are _not_ included in the clone. Internal stages are storage locations within Snowflake that hold data files. Since cloning is metadata-based, these data files are not duplicated. The clone has no internal stage associated with it. If you need to load data into the cloned database/schema, you'd need to create new internal stages within the clone.

External tables are also not cloned. An external table is essentially a metadata definition that points to data files stored outside of Snowflake (e.g., in S3, Azure Blob Storage, or Google Cloud Storage). Cloning the external table definition would simply create another pointer to the same external files, which is not the intended behaviour of a clone (and would create ambiguity).

  

**Question 20**

Incorrect

A data analyst needs to connect a business intelligence tool to Snowflake using the JDBC driver. The company uses SSO (Single Sign-On) for authentication. Which authenticator parameter value should be used in the JDBC connection string to enable SSO?

Choose **one** correct answer.

  

snowflake

Explanation

This option is used for username/password authentication, not SSO.

  

username_password_mfa

Explanation

Used to authenticate with MFA token caching. Read more on the Snowflake documentation page, [Using multi-factor authentication](https://docs.snowflake.com/en/developer-guide/jdbc/jdbc-configure.html#label-jdbc-multi-factor-auth)

**Correct answer**

  

externalbrowser

Explanation

This option enables SSO authentication by launching a browser window for login, making it the correct choice for SSO-based connections.

**Your answer is incorrect**

  

sso_enabled

Explanation

This is not a valid Snowflake JDBC authentication option.

Overall explanation

When connecting to Snowflake via JDBC, the authenticator parameter determines the authentication method. For SSO authentication, the correct value is externalbrowser, which redirects the user to a browser-based login.

Example connection string for SSO via JDBC:

jdbc:snowflake://mycompany.snowflakecomputing.com/?user=DATA_ANALYST&authenticator=externalbrowser

Using this option ensures secure SSO authentication while integrating client tools and applications with Snowflake.

  

Question 25

Incorrect

Which of the following is a valid Snowflake database name without requiring double quotes?

Choose **one** correct answer.

**Correct answer**

  

sales_db_

Explanation

This name starts with a letter and only contains letters, numbers, and underscores, making it valid without requiring double quotes.

**Your answer is incorrect**

  

2024_database

Explanation

Database names cannot start with a number unless enclosed in double quotes ("2024_database").

  

Overall explanation

In Snowflake, database names must start with a letter and can only contain letters, numbers, and underscores unless enclosed in double quotes (" "). If double quotes are used, the name becomes case-sensitive and can include special characters and spaces.

  

  

Question 29

Incorrect

You’re analyzing product purchase data in Snowflake and want to identify the most frequently purchased products across millions of rows without computing exact counts. Which function would allow you to estimate the most common product IDs efficiently?

Choose **one** correct answer.

  

COUNT

Explanation

As well as not being an estimation function, using COUNT alone to return the total number of rows doesn't help identify or rank the most frequent values.

**Your answer is incorrect**

  

APPROX_COUNT_DISTINCT

Explanation

This function estimates the number of distinct values, not their frequency.

**Correct answer**

  

APPROX_TOP_K

Explanation

APPROX_TOP_K is designed to estimate the most frequent values in a dataset. It is highly efficient for analyzing large volumes of data where exact results are less important than identifying top recurring items. For example, it’s ideal for finding the top 10 most purchased products or most common error codes.

  

TOP_N

Explanation

There is no built-in function called TOP_N in Snowflake.

Overall explanation

The APPROX_TOP_K function in Snowflake is an aggregate function used to efficiently estimate the most frequently occurring values in a dataset, along with their approximate frequencies. It is especially useful when working with very large datasets where calculating exact frequencies using standard aggregation (e.g., GROUP BY with COUNT) would be computationally expensive. Instead of returning precise results, APPROX_TOP_K uses the Space-Saving algorithm, which trades a small amount of accuracy for significant performance gains.

This function returns a JSON array of arrays, where each inner array contains two elements: the value and its estimated count. The number of top results to return is controlled by the parameter k, and the accuracy of the results can be tuned by increasing the counters parameter, which specifies how many distinct values to track internally.

Like in the Snowflake documentation, suppose you have a table lineitem with a column C4 representing item category codes. To find the top 3 most common categories, you could use:

- SELECT APPROX_TOP_K(C4, 3) AS top_categories
- FROM lineitem;

This might return a result like:

- [
- [1, 124923],
- [2, 107093],
- [3, 89438]
- ]

This output shows that category 1 occurred approximately 124,923 times, category 2 occurred about 107,093 times, and so on.

  

Question 30

Incorrect

What components make up a federated authentication environment in Snowflake?

Choose **two** correct answers.

**Correct selection**

  

Service Provider

Explanation

In a Snowflake federated authentication environment, Snowflake acts as the Service Provider (SP). It relies on a trusted Identity Provider to authenticate users and deliver assertions (via SAML 2.0) that Snowflake uses to grant access. The SP does not perform direct authentication but instead validates the identity assertion from the IdP.

**Your selection is incorrect**

  

Access Gateway

Explanation

Although access gateways are used in some enterprise architectures for routing authentication requests, Snowflake’s documentation does not define or require an access gateway as part of its federated authentication model.

**Your selection is correct**

  

Identity Provider

Explanation

The Identity Provider (IdP) is a third-party system (such as Okta and Microsoft AD FS) that authenticates users and sends SAML assertions to Snowflake. The IdP manages user credentials and authentication workflows, enabling Single Sign-On (SSO) for your Snowflake account.

  

Overall explanation

Federated authentication in Snowflake allows users to log in using their existing credentials from a separate, trusted system, rather than creating separate Snowflake usernames and passwords. This is achieved through the Security Assertion Markup Language (SAML) 2.0 standard, which defines how identity information is securely exchanged. The two core components involved are the Service Provider (SP), which in this case is Snowflake itself, and the Identity Provider (IdP). The IdP is a third-party system, such as Okta, Azure Active Directory, or PingFederate, that manages user identities and authenticates users.

The process works as follows: When a user attempts to access Snowflake, Snowflake (the SP) redirects the user to their organisation's IdP. The IdP authenticates the user (e.g., via username/password, multi-factor authentication). Upon successful authentication, the IdP sends a digitally signed SAML assertion back to Snowflake. This assertion contains information about the user's identity and attributes. Snowflake verifies the assertion's signature and validity, and if successful, grants the user access based on the information in the assertion. This enables Single Sign-On (SSO), centralised identity management, and enhanced security, as Snowflake does not store or manage user passwords directly. The benefit of this is a better security posture.

  

Question 32

Incorrect

You are using a COPY INTO <table> statement in Snowflake to load data from a stage. How would you correctly specify a named file format object called my_json_format to be used during the load?

Choose **one** correct answer.

**Your answer is incorrect**

  

COPY INTO my_table FROM @my_stage FILE_FORMAT = my_json_format;

Explanation

This syntax is invalid. To reference a named file format object, you must use the FORMAT_NAME keyword within the FILE_FORMAT parentheses. You cannot directly assign the format name.

  

COPY INTO my_table FROM @my_stage USE_FORMAT = my_json_format;

Explanation

USE_FORMAT is not a valid keyword in the COPY INTO statement.

**Correct answer**

  

COPY INTO my_table FROM @my_stage FILE_FORMAT = (FORMAT_NAME = my_json_format);

Explanation

Within the parentheses of the FILE_FORMAT option, FORMAT_NAME = my_json_format specifies the name of the pre-defined file format object.

  

COPY INTO my_table FROM @my_stage FORMAT = my_json_format;

Explanation

FORMAT is not the correct keyword to specify a file format object.

Overall explanation

Snowflake allows you to create named file format objects (using CREATE FILE FORMAT). These objects encapsulate a set of file format options. Here's an example from the Snowflake documentation showing how to create a file format object of type csv, with some other formatting options specified: 

- CREATE OR ALTER FILE FORMAT my_csv_format
- TYPE = CSV
- FIELD_DELIMITER = '|'
- SKIP_HEADER = 1
- NULL_IF = ('NULL', 'null')
- EMPTY_FIELD_AS_NULL = true
- COMPRESSION = gzip;

To use a named file format object within a COPY INTO statement, you use the FILE_FORMAT option, and within the parentheses, you use FORMAT_NAME = <your_format_name>. This tells Snowflake to use the options defined in that pre-existing file format object, rather than specifying the options directly within the COPY INTO statement. This promotes reusability and consistency. It contrasts with specifying options directly like FILE_FORMAT = (TYPE = JSON, FIELD_DELIMITER = '|'). You either use FORMAT_NAME or specify the individual options; you don't combine them.

  

  

Question 34

Incorrect

Which of the following are **limitations** when creating materialized views in Snowflake?

Choose **two** correct answers.

**Your selection is correct**

  

They cannot include JOIN operations

Explanation

Materialized views are maintained automatically using Snowflake-managed resources, not your own virtual warehouses. Compute from your own virtual warehouse is not used unless you're querying the view directly.

**Your selection is incorrect**

  

They cannot reference a masking policy on one of their columns

Explanation

Masking policies can be applied to columns in materialized views. Snowflake supports this as part of its data governance capabilities.

**Correct selection**

  

They cannot include ORDER BY clauses

Explanation

Operations like viewing or altering metadata are technically an activity which falls under Cloud Services Compute, which is not directly relevant when discussing billing for materialized views.

  

Overall explanation

Materialized views in Snowflake act as **physically stored, pre-computed tables** derived from SELECT queries, unlike standard views which are just stored query definitions. This architecture delivers faster query performance by avoiding repeated computation, especially for expensive aggregations or projections.

To support **incremental refreshes**—so only changed data is updated—Snowflake imposes restrictions on materialized view definitions. You can query **only one base table**; complex features like joins, window functions, non-deterministic functions (e.g., CURRENT_TIMESTAMP), DISTINCT in aggregate expressions, ORDER BY, or LIMIT are disallowed. These constraints ensure efficient refresh and reliable automatic query rewrite by the optimizer

  

  

Question 41

Incorrect

Which of the following CREATE TABLE statements correctly defines a table with: 

1. A numeric column that accepts a ten-digit integer.  
    
2. A string column that, by default, accepts only one character.  
    
3. A date column for storing dates without time elements.  
    

Choose **one** correct answer.

**Correct answer**

  

- CREATE TABLE example (
- num_col NUMBER(10,0),
- str_col CHAR,
- date_col DATE
- );

Explanation

1. NUMBER(10,0) defines a numeric column that can store integers up to 10 digits without decimal places.  
    
2. CHAR defaults to a length of 1 when no length is specified, thus accepting a single character by default.  
    
3. DATE is used to store dates without time elements.  
    

Question 42

Incorrect

In Snowflake, which two SQL commands can be used to assign a tag to an object?

Choose **two** correct answers.

**Your selection is correct**

  

CREATE TABLE employees (id INT, name STRING) TAG (sensitive_data = 'PPI');

Explanation

In Snowflake, you can assign a tag to an object at the time of its creation using the TAG clause within the CREATE statement. This command creates the employees table and assigns the tag sensitive_data with the value 'PPI' to it.

**Correct selection**

  

ALTER TABLE employees SET TAG sensitive_data = 'PPI'; 

Explanation

To assign a tag to an existing object, you use the ALTER statement with the SET TAG clause. This command assigns the tag sensitive_data with the value 'PPI' to the existing employees table.

  

Overall explanation

Tags are schema-level objects that can be assigned to various database objects to facilitate data classification, governance, and security. You can assign tags during object creation using the TAG clause within the CREATE statement or to existing objects using the ALTER statement with the SET TAG clause. This allows for consistent metadata management and enhances data governance practices within the Snowflake environment.

  

  

**Question 43**

Incorrect

In Snowflake, when you apply a tag to a table, how does it affect the table's columns?

Choose **one** correct answer.

  

**Correct answer**

  

The columns inherit the tag automatically, and the inherited tag values can be overridden at the column level

Explanation

When a tag is applied to a table, it is inherited by all columns. Snowflake also allows you to override the tag’s value at the column level if needed.

  

The tag is only applied to columns if they share the same data type as the tagged table

Explanation

Tag inheritance is not determined by data type. All columns, regardless of type, inherit the tag when it’s applied to their parent table.

Overall explanation

In Snowflake, assigning a tag to a table automatically causes that tag to be inherited by all of its columns — a feature known as **tag lineage**. Importantly, Snowflake also supports overriding the inherited tag value at the column level, providing flexibility for more granular data classification.

Assigning the sensitivity tag to a table:

- ALTER TABLE customer_data SET TAG sensitivity = 'high';

All columns in customer_data will now inherit the sensitivity='high' tag. To override the tag value for a specific column (e.g., email):

- ALTER TABLE customer_data MODIFY COLUMN email SET TAG sensitivity = 'medium';

This mechanism supports precise governance of sensitive information while maintaining consistency across the schema.

  

Question 45

Incorrect

Which privilege allows a role in Snowflake to drop, alter, and grant or revoke access to an object?

Choose **one** correct answer.

  

USAGE

Explanation

The USAGE privilege allows limited interaction with an object (e.g., referencing a database or schema), but does not allow modifying, dropping, or controlling access to it.

**Correct answer**

  

OWNERSHIP

Explanation

The OWNERSHIP privilege gives full control over an object, including the ability to drop it, alter its structure, and grant or revoke access to other roles. It is the highest level of privilege for a specific object.

  

MODIFY

Explanation

MODIFY allows structural changes to certain objects (like adding columns to a table), but it does not allow dropping the object or managing access (granting/revoking).

**Your answer is incorrect**

  

MANAGE GRANTS

Explanation

MANAGE GRANTS "[enables granting or revoking privileges on objects for which the role is not the owner](https://docs.snowflake.com/en/user-guide/security-access-control-privileges)."

Overall explanation

The OWNERSHIP privilege grants full control over a specific object—it allows a role to modify, drop, rename, and manage access by granting or revoking privileges. Only one role can own an object at any time, and this role can transfer ownership to another role using GRANT OWNERSHIP.

By default, the **creator's active primary role** becomes the owner. Ownership can also be delegated to database roles and shared across users carrying the same role, centralizing control to align with security best practices.

Here’s how an administrator can transfer ownership:

- GRANT OWNERSHIP
- ON TABLE customer_data
- TO ROLE DBA_ROLE
- COPY CURRENT GRANTS;

This command transfers complete control, including existing grants, from the current owner to DBA_ROLE

  

  

Question 47

Incorrect

Which of the following account objects **cannot be replicated** across accounts using Snowflake’s account replication feature?

Choose **one** correct answer.

  

Roles

Explanation

Snowflake can replicate roles (and other granted privileges) to another account, provided you are on Business Critical edition . Roles are considered account objects, and when included in a replication or failover group, the entire role hierarchy and grants are copied over to the secondary account.

  

Resource monitors

Explanation

Resource monitors objects (which monitor credit usage) can be replicated but Business Critical edition is required. If you include resource monitors in a replication group, the definitions (e.g., a monitor limiting warehouse credits per month) will be copied to the secondary account.

**Correct answer**

  

Inbound shares

Explanation

Inbound shares cannot be replicated to another account. Snowflake documentation states that you can only replicate outbound shares (shares you create), and “[Replication of inbound shares (shares from providers) is not supported.](https://docs.snowflake.com/en/user-guide/account-replication-intro#replicated-objects)” 

**Your answer is incorrect**

  

Warehouses

Explanation

Virtual warehouse objects are replicable with Business Critical edition and higher. When warehouses are included in a replication group, the secondary account will have the same warehouse configurations (name, size, etc.), although they won’t start automatically running — you would still need to resume them as needed.

Overall explanation

Snowflake’s account replication can copy many types of objects (databases, roles, etc.) to another account, but there are a few things it cannot replicate.  Inbound shares (data shared to you from another account) are not replicated. In a real scenario, this affects disaster recovery planning. For example, if your primary account consumes a Snowflake Marketplace dataset (an inbound share), that shared data will not automatically appear in your secondary account upon replication – the provider would need to share it separately to the secondary. Understanding this helps avoid surprises when failing over.

  

  

Question 52

Incorrect

Within a Snowflake Scripting block, how can you include the value of a local variable in an SQL statement?

Choose **one** correct answer.

  

Enclose the variable name in quotes in the SQL statement

Explanation

Quoting the variable name (e.g., 'my_var' or "my_var") would turn it into a string literal or identifier in the SQL, not use the variable’s value.

  

Use the variable name in the SQL statement without any prefix

Explanation

If you just wrote the name of a variable, the query engine would treat it as an identifier (e.g., a column or literal) rather than a variable reference. The colon prefix is needed to let Snowflake know it’s a bind variable in the script .

**Your answer is incorrect**

  

Prefix the variable name with a dollar sign (e.g., $my_var)

Explanation

A dollar sign denotes a session SQL variable in Snowflake (used outside of scripting blocks). Within a Snowflake Scripting block, $my_var would not refer to a local variable.

**Correct answer**

  

Prefix the variable name with a colon (e.g., :my_var)

Explanation

Using a colon before the variable name is the required syntax to bind a variable’s value into an SQL statement in Snowflake Scripting . For example, INSERT INTO table VALUES(:my_var) will insert the value of my_var.

Overall explanation

To bind a Snowflake Scripting variable into a SQL statement, you prepend a colon (:) to the variable name . Here we're inserting the variable variable1 into a table t's column c1:

-- Create a simple table for demonstration

CREATE OR REPLACE TABLE t (

c1 STRING

);

-- Begin Snowflake Scripting block

DECLARE variable1 STRING;

BEGIN

-- Assign a value to the scripting variable

LET variable1 = 'Hello, Snowflake!';

-- Use the variable in an INSERT statement via bind notation

INSERT INTO t (c1) VALUES (:variable1);

-- Optionally, confirm the insert by selecting the row

RETURN (SELECT 'Inserted value: ' || c1 FROM t ORDER BY c1 DESC LIMIT 1);

END;

  

  

Question 63

Incorrect

To generate unique order IDs that start at 5000 and increment by 5, which of the following statements correctly creates this sequence in Snowflake?

Choose **one** correct answer.

**Correct answer**

  

CREATE SEQUENCE order_id_seq START = 5000 INCREMENT = 5;

Explanation

This statement uses valid Snowflake syntax to create a sequence starting at 5000 and incrementing by 5.

  

  

Overall explanation

In Snowflake, sequences are schema-level objects designed to generate unique numeric values, commonly used for surrogate keys or unique identifiers. To create a sequence with a specific starting point and increment, you can use the CREATE SEQUENCE statement with either START = or START WITH, and INCREMENT = or INCREMENT BY. 

For example, to create a sequence named order_id_seq that starts at 5000 and increments by 5: 

- CREATE SEQUENCE order_id_seq START = 5000 INCREMENT = 5;

This sequence will generate values like 5000, 5005, 5010, and so on. 

It's important to use the correct syntax as per Snowflake's documentation to ensure the sequence behaves as intended.

  

  

Question 65

Incorrect

What is the maximum file size (in MB) allowed when uploading files through Snowsight for data loading?

Choose **one** correct answer.

**Your answer is incorrect**

  

100

Explanation

This is below the actual limit and may unnecessarily restrict usability.

**Correct answer**

  

250

Explanation

Snowsight (the Snowflake Web UI) allows uploading individual files up to **250 MB** in size. You can upload up to **250 files** at a time.

  

Overall explanation

Snowsight is Snowflake’s modern web-based interface for loading and managing data. When using Snowsight to load data:

- You can upload up to 250 files at once  
    
- Each file must be ≤ 250 MB  
    
- To upload larger files or bulk load many files, it’s recommended to use SnowSQL or stage the files in cloud storage (e.g., AWS S3, Azure Blob, GCP buckets) and use COPY INTO.  
    

For example, if you need to upload ten 300 MB files, you can't use Snowsight. You must use SnowSQL or external staging.

  

**Question 67**

Incorrect

Which Snowflake-provided system function must be executed to generate the input file required by SnowCD for connectivity checks?

Choose **one** correct answer.

  

Overall explanation

To run **SnowCD** you must first generate a list of hostnames and ports that your client environment should be able to reach in order to connect to Snowflake services.

This is done by executing the function:

SELECT SYSTEM$ALLOWLIST();

This returns a JSON array of host-port pairs similar to:

[

{ "type": "STAGE", "host": "mybucket.s3.us-west-2.amazonaws.com", "port": 443 },

{ "type": "SNOWSQL_REPO", "host": "repo.snowflakecomputing.com", "port": 443 },

{ "type": "OCSP_CACHE", "host": "ocsp.snowflakecomputing.com", "port": 80 }

]

You should save this output to a file (e.g. allowlist.json).

Then, run SnowCD using this file:

  

**snowcd allowlist.json**

  

This command checks DNS resolution, port connectivity, and HTTP-level access for each listed endpoint.

You want to verify that a new server in your environment can reach all required Snowflake services before running a workload or need to debug a connection failure and want to confirm whether it's a DNS or firewall issue.

SnowCD will return All checks passed if everything is reachable and a detailed failure output with suggestions (e.g. DNS resolution failed, port unreachable, invalid certificate, etc.) if something is misconfigured.

  

  

  

Question 68

Incorrect

Which of the following is a valid SnowSQL client-side command used to set configuration options?

Choose **one** correct answer.

Overall explanation

SnowSQL includes a set of non-SQL, client-side commands prefixed with !. These commands allow users to manage their SnowSQL session itself — separate from interacting with the Snowflake database.

Examples include:

- !set – set SnowSQL configuration options (e.g., !set output_format=csv)  
    
- !define – define substitution variables  
    
- !help – list available ! commands  
    
- !queries – view query history  
    
- !quit / !exit – exit the SnowSQL session  
    
- !source / !load – run a SQL script file  
    

These are interpreted by the SnowSQL CLI and are not executed as SQL in the Snowflake backend.

  

  

Question 76

Incorrect

The SEED (or REPEATABLE) parameter is used to make table sampling deterministic. Which **sampling methods** support the use of this parameter?

Choose **one** correct answer.

  

Overall explanation

The SAMPLE (or TABLESAMPLE) clause allows you to return a subset of rows from a table using different methods:

- BERNOULLI / ROW — Samples each row independently with a specified probability.  
    
- SYSTEM / BLOCK — Samples blocks of rows with a specified probability. Faster on large tables but can be biased on small ones.  
    

To make sampling deterministic (i.e., to return the same sample set when a query is re-executed), you must use the SEED or REPEATABLE parameter. This only works with SYSTEM sampling — not BERNOULLI, not ROW, and not in subqueries or views.

  

**1) BERNOULLI / ROW (row-by-row probability)**

  

-- About ~10% of rows; each row is included independently (Bernoulli).

SELECT c_custkey, c_name, c_nationkey

FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER

SAMPLE BERNOULLI (10);      -- or simply: SAMPLE (10)

Expected size ≈ 10% of the table. No seed support here. [Snowflake Docs](https://docs.snowflake.com/en/sql-reference/constructs/sample)  

**2) SYSTEM / BLOCK (block sampling; faster on big tables)**

  

-- About ~5% of data blocks; good performance on large tables,

-- but can be biased on small tables.

SELECT o_orderkey, o_custkey, o_totalprice

FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS

TABLESAMPLE SYSTEM (5);

Samples whole storage blocks; may be biased for small tables. [Snowflake Docs](https://docs.snowflake.com/en/sql-reference/constructs/sample)  

**3) Deterministic sampling (SEED / REPEATABLE) — only with SYSTEM**

  

-- Re-running this returns the SAME sample (as long as the table doesn’t change).

SELECT l_orderkey, l_partkey, l_extendedprice

FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM

SAMPLE SYSTEM (3) SEED (42);          -- REPEATABLE (42) is synonymous

SEED/REPEATABLE works **only** with SYSTEM|BLOCK and **not** with BERNOULLI|ROW.  

Not supported in subqueries or views, and not with fixed-size samples (... ROWS). [Snowflake Docs](https://docs.snowflake.com/en/sql-reference/constructs/sample)  

**Handy notes**

SAMPLE and TABLESAMPLE are synonyms; likewise BERNOULLI|ROW, SYSTEM|BLOCK, SEED|REPEATABLE. [Snowflake Docs](https://docs.snowflake.com/en/sql-reference/constructs/sample)  

Fixed-size example (no seed):  
  
  
  
SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER SAMPLE (100 ROWS);

  
  
  
(SEED not allowed with fixed-size, and SYSTEM doesn’t support fixed-size at all.) [Snowflake Docs](https://docs.snowflake.com/en/sql-reference/constructs/sample)

  

  

Question 78

Incorrect

On which of the following object types can you create a Snowflake stream?

Choose **three** correct answers.

**Your selection is incorrect**

  

Stages

Explanation

Stages are file storage locations used for bulk loading or unloading data. They do not support change tracking via streams.

**Correct selection**

  

Views

Explanation

Streams can be created on both standard and secure views, allowing you to capture changes through a logical layer over a table.

**Your selection is correct**

  

Standard tables

Explanation

Streams are most commonly created on standard tables to track DML changes like INSERTs, UPDATEs, and DELETEs.

**Your selection is correct**

  

External tables

Explanation

Streams support external tables, including those referencing files in cloud storage like Amazon S3. They enable change tracking of new or updated files.

  

Materialized views

Explanation

Streams don't yet have the ability to track changes in materialized views

  

Masking policies

Explanation

These are data governance tools used to obfuscate sensitive data and are not involved in tracking data changes on a table.

Overall explanation

In Snowflake, streams capture change data for use cases like incremental ETL, data auditing, or reactive pipelines. You can create a stream on:

- Standard tables, including shared ones  
    
- Views, including secure views  
    
- External tables  
    
- Event tables  
    
- Iceberg tables  
    
- Dynamic tables  
    
- Directory tables  
    

Here's some sample code for creating a stream on a table called orders:

- CREATE OR REPLACE STREAM order_stream ON TABLE orders;

This lets you track every row inserted, updated, or deleted from the orders table since the last stream consumption.

  

  

**What each one is**

**External table**: a database object that lets you **query data files** (Parquet/CSV/JSON, etc.) that live in an **external stage** (S3/Blob/GCS) as if they were a table. Read-only; Snowflake scans the files at query time. [Snowflake Documentation+1](https://docs.snowflake.com/en/user-guide/tables-external-intro?utm_source=chatgpt.com)  

**Directory table**: not a “table” you create with DDL—it's **metadata that Snowflake maintains for a stage** (internal or external) listing the **files in that stage** (name, size, last modified, URL, checksum). You query it with the DIRECTORY(@stage) table function. [Snowflake Documentation+1](https://docs.snowflake.com/en/user-guide/data-load-dirtables?utm_source=chatgpt.com)  

**Core differences (at a glance)**

**Purpose**

External table → query **data content** from files (analytics without loading). [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/tables-external-intro?utm_source=chatgpt.com)  

Directory table → query **file inventory/metadata** (what files exist, when modified, build pipelines). [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/data-load-dirtables?utm_source=chatgpt.com)  

**How you query**

External table → SELECT … FROM my_ext_table (columns parsed via file format; often a VARIANT). [Snowflake Documentation](https://docs.snowflake.com/en/en/sql-reference/sql/create-external-table?utm_source=chatgpt.com)  

Directory table → SELECT * FROM DIRECTORY(@my_stage) (returns file rows, not data records). [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/data-load-dirtables-query?utm_source=chatgpt.com)  

**DML**

External table → **read-only** (no INSERT/UPDATE/DELETE). [Chaos Genius](https://www.chaosgenius.io/blog/snowflake-external-tables/?utm_source=chatgpt.com)  

Directory table → also read-only; it’s a view of stage metadata.  

**Where they live**

External table → real schema object with privileges. [Snowflake Documentation](https://docs.snowflake.com/en/en/sql-reference/sql/create-external-table?utm_source=chatgpt.com)  

Directory table → **layer on a stage**; enabled with CREATE STAGE … DIRECTORY = (ENABLE = TRUE). [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/data-load-dirtables-manage?utm_source=chatgpt.com)  

**Refresh behavior**

External table → metadata management depends on auto-refresh/events or manual refresh depending on setup/cloud. (Docs cover the intro and pattern.) [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/tables-external-intro?utm_source=chatgpt.com)  

Directory table → internal stages need **manual** ALTER STAGE … REFRESH; external stages can be manual or **automated** refresh. [Snowflake Documentation+1](https://docs.snowflake.com/en/user-guide/data-load-dirtables-manage?utm_source=chatgpt.com)  

**Good for**

External table → keep data in your lake, query/join in Snowflake without loading. [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/tables-external-intro?utm_source=chatgpt.com)  

Directory table → replace LIST @stage with SQL-able metadata for **pipelines**, joins to control tables, and **unstructured data** discovery. [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/data-load-dirtables?utm_source=chatgpt.com)  

**Tiny examples**

**External table (query file contents):**

  

CREATE EXTERNAL TABLE ext.sales_parquet

  WITH LOCATION = @my_ext_stage/sales/

  FILE_FORMAT = (TYPE = PARQUET);

  

SELECT * FROM ext.sales_parquet WHERE amount > 100;

(Reads rows from Parquet files in the stage.) [Snowflake Documentation](https://docs.snowflake.com/en/en/sql-reference/sql/create-external-table?utm_source=chatgpt.com)

**Directory table (list files & metadata):**

  

-- Stage with directory table enabled

CREATE STAGE my_int_stage DIRECTORY = (ENABLE = TRUE);

  

-- Keep metadata current (internal stages)

ALTER STAGE my_int_stage REFRESH;

  

-- Query file inventory

SELECT * FROM DIRECTORY(@my_int_stage)

WHERE RELATIVE_PATH LIKE 'sales/%' ORDER BY LAST_MODIFIED DESC;

(Returns one row per file with size, last modified, Snowflake file URL, etc.) [Snowflake Documentation+1](https://docs.snowflake.com/en/user-guide/data-load-dirtables-manage?utm_source=chatgpt.com)

  

Question 86

Incorrect

When creating a UDF (user-defined function) in Snowflake, which three languages allow the handler code to be **staged** instead of kept fully in-line in the CREATE FUNCTION statement?

Choose **three** correct answers.

  

Overall explanation

When creating UDFs (user-defined functions) in Snowflake, the handler code (the actual logic) can either be **in-line** (written directly in the CREATE FUNCTION statement), or **staged** (uploaded to a Snowflake stage, and referenced in the function definition).

SQL and JavaScript UDFs must have the logic written directly in the statement (in-line).

Java, Python, and Scala UDFs allow you to either write the logic in-line, or upload compiled source code or modules (like .jar or .py files) to a stage and reference it.

Here's an example creating a Java UDF with staged code:

CREATE OR REPLACE FUNCTION multiply_numbers(x INT, y INT)

RETURNS INT

LANGUAGE JAVA

RUNTIME_VERSION = '11'

IMPORTS = ('@my_stage/my_math_utils.jar')

HANDLER = 'com.example.MathUtils.multiply';

  

IMPORTS = ('@my_stage/my_math_utils.jar') tells Snowflake where to find the staged JAR file containing the compiled Java code. The @my_stage refers to a named Snowflake stage.

HANDLER = 'com.example.MathUtils.multiply' points to the fully qualified class and method name inside the JAR file that implements the function logic.

  

  

**Exam - 5**

  

**Question 11**

Incorrect

How can we tell in the Query Profile tool on the Snowsight UI if a query is using the Metadata Cache?

Choose **one** correct answer.

**Correct answer**

  

An operator titled METADATA-BASED RESULT is returned

Explanation

This is the definitive indicator that a query has retrieved results using Snowflake's metadata cache. When this operator appears in the Query Profile, it means that the query results were generated entirely from metadata rather than scanning actual table data. This applies to queries like SELECT COUNT(*) FROM table_name, which Snowflake can fulfill using stored metadata rather than reading the full dataset.

  

An operator titled QUERY RESULT REUSE is returned

Explanation

While query result reuse does improve performance, it is not the same as metadata cache usage.

**Your answer is incorrect**

  

An operator titled TableScan with the Bytes scanned statistic showing 0MB is returned

Explanation

A TableScan operator with 0MB scanned suggests that Snowflake pruned unnecessary partitions or used result caching, but it does not confirm metadata cache usage. Metadata cache queries do not require a TableScan operator at all—only the METADATA-BASED RESULT operator.

  

Overall explanation

Snowflake optimizes performance by storing table metadata (e.g., row counts, min/max values) separately from actual table data in the metadata cache in the services layer of Snowflake's multi-cluster shared disk architecture. Queries that can be resolved using only metadata are much faster because they avoid scanning any table data.

To determine if a query used metadata cache, check the Query Profile tool for a specific query in Snowsight by looking for the METADATA-BASED RESULT operator. Here's what the operator looks like:

  

  

  

  

Question 13

Incorrect

How can you configure a Snowflake session to disable the use of cached query results?

Choose **one** correct answer.

**Correct answer**

  

ALTER SESSION SET USE_CACHED_RESULT = FALSE;

Explanation

The USE_CACHED_RESULT parameter controls whether Snowflake reuses cached query results. Setting it to FALSE ensures that each query is executed anew, regardless of existing cached results.

**Your answer is incorrect**

  

ALTER SESSION SET ENABLE_QUERY_CACHE = FALSE;

  

Overall explanation

In Snowflake, query result caching enhances performance by storing the results of executed queries for reuse. By default, this feature is enabled, meaning that if an identical query is executed and the underlying data hasn't changed, Snowflake retrieves the result from the cache, reducing execution time. However, there are scenarios, such as performance benchmarking or ensuring real-time data retrieval, where you might want to disable this feature forcing "[Snowflake to execute each query when submitted, regardless of whether a matching query result exists.](https://docs.snowflake.com/en/sql-reference/parameters#label-use-cached-result)"

Here are some code examples showing you how to set the USE_CACHED_RESULT parameter to FALSE at different levels: 

- Session Level: Applies the setting to the current session. 

- ALTER SESSION SET USE_CACHED_RESULT = FALSE;  
    

- User Level: Applies the setting to all sessions initiated by the user. 

- ALTER USER <username> SET USE_CACHED_RESULT = FALSE;  
    

- Account Level: Applies the setting globally across the entire account. 

- ALTER ACCOUNT SET USE_CACHED_RESULT = FALSE;  
    

Adjusting this parameter ensures that queries fetch the most current data by executing fully, bypassing any cached results.

  

  

Question 16

Incorrect

Which factors can lead to the degradation of a table's natural clustering in Snowflake?

Choose **two** correct answers.

**Correct selection**

  

The size of the table

Explanation

As a table's size increases, particularly when it grows to several terabytes, its natural clustering can degrade. This degradation occurs because larger tables are more prone to data distribution issues, leading to inefficient data retrieval.

**Your selection is correct**

  

The number of DML statements performed against the table

Explanation

Frequent DML operations, such as inserts, updates, and deletes, can disrupt the natural clustering of a table. These operations can cause data to be stored in a less organized manner, negatively impacting query performance.

  

Overall explanation

Natural clustering refers to how well-ordered data is stored within micro-partitions. Efficient clustering improves query performance by reducing the number of partitions scanned. However, two primary factors cause clustering to degrade:

1. Table Size:

- As a table grows larger, its natural ordering may become less efficient due to the increasing number of micro-partitions.  
    
- This results in wider partition scans during queries, which slows performance.  
    

3. Frequent DML Operations:

- Repeated INSERT, UPDATE, and DELETE operations cause Snowflake to create new micro-partitions.  
    
- These new partitions may not align well with the original partition structure, leading to suboptimal clustering.  
    

To prevent degradation, Snowflake offers automatic clustering and user-defined clustering keys to reorganise data efficiently over time.

  

Question 17

Incorrect

In Snowflake, how does the cardinality of a column affect the effectiveness of micro-partition pruning?

Choose **one** correct answer.

  

Overall explanation

Micro-partition pruning leverages metadata about the minimum and maximum values of columns within micro-partitions to optimize query performance by scanning only relevant partitions, and retrieving only those from remote storage. The cardinality of a column—referring to the number of distinct values it contains—significantly impacts the effectiveness of this pruning: 

- Low Cardinality: Columns with few distinct values (e.g., a Boolean column) may result in many micro-partitions containing the same values, limiting pruning efficiency.  
    
- High Cardinality: Columns with many distinct values (e.g., a column with unique identifiers) can make clustering maintenance costly and may not provide substantial pruning benefits. "[For example, a column that contains nanosecond timestamp values would not make a good clustering key.](https://docs.snowflake.com/en/user-guide/tables-clustering-keys#strategies-for-selecting-clustering-keys)"  
    

Therefore, selecting columns with moderate cardinality as clustering keys is advisable to enhance micro-partition pruning and, consequently, query performance.

  

Question 18

Incorrect

If a view is created with a masking policy on one of its columns, and that view also references a table column that **already** has a masking policy, which masking policy is applied when the view is queried?

Choose **one** correct answer

  

Overall explanation

When a view references a table column that already has a masking policy, the table-level policy is enforced first. Even if a separate masking policy is applied to the view, it does not override the policy on the table.

Let's look at a scenario:

A table has a masking policy applied to the ssn column:

CREATE MASKING POLICY ssn_masking_policy AS (val STRING) RETURNS STRING -> 

CASE WHEN CURRENT_ROLE() = 'HR_ADMIN' THEN val ELSE 'XXX-XX-' || RIGHT(val, 4) END;

ALTER TABLE employees MODIFY COLUMN ssn SET MASKING POLICY ssn_masking_policy;

A view is created from this table, and a different masking policy is applied at the view level:

CREATE MASKING POLICY view_masking_policy AS (val STRING) RETURNS STRING -> 

CASE WHEN CURRENT_ROLE() = 'DATA_ANALYST' THEN val ELSE 'MASKED' END;

CREATE VIEW employees_view AS SELECT * FROM employees;

ALTER VIEW employees_view MODIFY COLUMN ssn SET MASKING POLICY view_masking_policy;

When a DATA_ANALYST queries the view:

SELECT ssn FROM employees_view;

The table-level masking policy is enforced before the data reaches the view.  

Since the table already masked the SSN as "XXX-XX-6789", the view’s masking policy does not further modify it.  

The output remains "XXX-XX-6789", not "MASKED" as defined in the view’s policy.  

  

  

  

**ChatGPT disagrees**

  

Short answer: **No—your example is not correct.**  
When a view column has its **own masking policy**, that **view-level policy is the one that runs** for queries against the view. The table’s masking policy does **not** run “first,” and policies don’t stack. Snowflake rewrites the query **once per column occurrence** using the policy bound to that column (view if present; otherwise the table’s). [Snowflake Documentation+1](https://docs.snowflake.com/en/user-guide/security-column-ddm-use?utm_source=chatgpt.com)

**Corrected walk-through**

  

-- Table policy (masks unless HR_ADMIN)

CREATE OR REPLACE MASKING POLICY ssn_masking_policy AS (val STRING) RETURNS STRING ->

  IFF(IS_ROLE_IN_SESSION('HR_ADMIN'), val, 'XXX-XX-' || RIGHT(val, 4));

  

CREATE OR REPLACE TABLE employees (emp_id INT, ssn STRING);

ALTER TABLE employees MODIFY COLUMN ssn SET MASKING POLICY ssn_masking_policy;

  

-- View over the table

CREATE OR REPLACE VIEW employees_view AS SELECT emp_id, ssn FROM employees;

  

-- View policy (masks unless DATA_ANALYST)

CREATE OR REPLACE MASKING POLICY view_masking_policy AS (val STRING) RETURNS STRING ->

  IFF(IS_ROLE_IN_SESSION('DATA_ANALYST'), val, 'MASKED');

  

-- Attach policy to the VIEW column

ALTER VIEW employees_view MODIFY COLUMN ssn SET MASKING POLICY view_masking_policy;

**What happens when querying the view:**

- A user with DATA_ANALYST active runs SELECT ssn FROM employees_view;  
    → **view_masking_policy** decides the output. If it returns the raw value, the SSN is shown in full—even though the table has a different policy.  
    
- A user without DATA_ANALYST active sees 'MASKED' from the **view policy**.  
    
- The table policy is only used when selecting from **employees** directly or when a view **does not** have its own policy on that column. [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/security-column-ddm-use?utm_source=chatgpt.com)  
    

**How to verify which policy applies**

- DESCRIBE VIEW employees_view; shows the **POLICY NAME** on each column (if any).  
    
- DESCRIBE TABLE employees; shows the policy on the table column.  
    These help confirm that the view column has its own policy and thus governs queries against the view. [Snowflake Documentation](https://docs.snowflake.com/en/en/sql-reference/sql/desc-view?utm_source=chatgpt.com)  
    

Tip: prefer IS_ROLE_IN_SESSION('ROLE') over CURRENT_ROLE() in policies so secondary roles are honored. And remember: you can attach masking policies to **tables or views**—they’re mutually exclusive per column reference at query time. [Snowflake Documentation](https://docs.snowflake.com/en/sql-reference/sql/create-masking-policy?utm_source=chatgpt.com)

  

  

Question 32

Incorrect

On which of the following Snowflake objects/statements relevant to data loading can file format options be specified?

Choose **three** correct answers.

  

  

Overall explanation

Snowflake provides flexibility in how you define the format of the files you're loading (e.g., CSV, JSON, Parquet, Avro, ORC, XML). These file format options control how Snowflake interprets the data within those files – things like the delimiter used in a CSV file, whether to skip header rows, how to handle null values, and so on. Crucially, you can specify these options at multiple levels related to data loading:

1. Stages: When you create a stage (using CREATE STAGE), you can define file format options directly within the stage definition. These options then apply by default to all files loaded from that stage, unless overridden at a lower level. An example from the [Snowflake documentation](https://docs.snowflake.com/en/sql-reference/sql/create-stage#basic-examples):

- CREATE TEMPORARY STAGE my_int_stage
- FILE_FORMAT = (TYPE = CSV);

3.   
      
      
    
4. Pipes: A pipe (created with CREATE PIPE) includes a COPY INTO statement. You can specify file format options within this embedded COPY INTO command. These options apply specifically to the data loading process managed by that pipe. An example from the [Snowflake documentation](https://docs.snowflake.com/en/sql-reference/sql/create-pipe#examples):

- CREATE PIPE mypipe
- AS
- COPY INTO mytable
- FROM @mystage
- FILE_FORMAT = (TYPE = 'JSON');

6.   
      
      
    
7. COPY INTO Statements: Whether you're using a standalone COPY INTO <table> command or the one embedded within a pipe, you can specify file format options directly within the statement itself. An example from the [Snowflake documentation](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table#examples):

- COPY INTO mytable
- FILE_FORMAT = (TYPE = CSV);

9.   
      
      
    

Snowflake applies file format options in the following order, from most specific to least specific: COPY INTO Statement (Highest Precedence) -> Pipe (Medium Precedence) -> Stage (Lowest Precedence). If no options are applied, Snowflake will use the default values.

  

  

Question 35

Incorrect

Which Account Usage view in Snowflake can be used to monitor the billing and maintenance activity of a materialized view?

Choose **one** correct answer.

  

QUERY_HISTORY

Explanation

This view tracks SQL queries executed in your account but does not contain specific information about materialized view maintenance or billing.

**Correct answer**

  

MATERIALIZED_VIEW_REFRESH_HISTORY

Explanation

This Account Usage view provides billing information about automatic refresh operations of materialized views, including timestamps and credit usage, making it ideal for monitoring billing impact from Snowflake-managed compute resources.

  

Question 36

Incorrect

Which of the following types of metadata does Snowflake store for each micro-partition file?

Choose **two** correct answers.

**Your selection is correct**

  

The range of values for each column

Explanation

Snowflake stores the minimum and maximum values for each column within a micro-partition. This enables efficient query performance through partition pruning, which helps eliminate unnecessary calls to remote storage.

  

The average row length in the partition

Explanation

While row size may affect compression, Snowflake doesn’t store average row length in micro-partition metadata. It’s not used for pruning or query optimization directly.

**Correct selection**

  

The number of distinct values in each column

Explanation

This metadata helps when a query asks for COUNT(DISTINCT column) on a table, Snowflake can, in many cases, determine the exact distinct count without scanning the actual data in the micro-partitions. It simply sums the distinct value counts from the metadata of the relevant micro-partitions

**Your selection is incorrect**

  

The most frequent value per column

Explanation

Snowflake does not track frequency distributions at the micro-partition level. Although this information could theoretically help with optimization, it’s not part of the stored metadata.

  

  

Question 39

Incorrect

An administrator would like to control which MFA methods users are allowed to use as a second factor of authentication. How would they achieve this?

Choose **one** correct answer.

  

By modifying the user's role assignment

Explanation

Roles control permissions, not authentication behavior.

**Correct answer**

  

By creating or updating an authentication policy

Explanation

Snowflake uses **authentication policies** to define which MFA methods are allowed (e.g., PASSKEY, TOTP, DUO). This is the documented and supported way to enforce MFA method restrictions.

  

Overall explanation

The CREATE AUTHENTICATION POLICY command lets administrators define how users authenticate. It controls allowed login methods (e.g., PASSWORD, SAML, OAUTH), enforces MFA enrollment, and restricts which MFA methods (e.g., PASSKEY, TOTP, DUO) can be used.

Once created, the policy must be assigned to a user or account using ALTER USER or ALTER ACCOUNT to take effect.

To allow only password-based logins with mandatory MFA, and restrict second factors to passkeys and authenticator apps (excluding Duo):

- CREATE AUTHENTICATION POLICY enforce_mfa_policy
- AUTHENTICATION_METHODS = ('PASSWORD')
- MFA_ENROLLMENT = REQUIRED
- MFA_POLICY = (ALLOWED_METHODS = ('PASSKEY', 'TOTP'));

Then apply it with:

- ALTER ACCOUNT SET AUTHENTICATION_POLICY = enforce_mfa_policy;

This ensures secure, policy-driven access tailored to your organization's MFA preferences.

  

  

Question 42

Incorrect

Given the following GeoJSON data representing a geographical point with standard longitude and latitude coordinates:

{

"type": "Point",

"coordinates": [-122.4194, 37.7749]

}

Which data type in Snowflake is most appropriate for storing this data to ensure accurate geospatial calculations on the Earth's surface?

Choose **one** correct answer.

  

VARCHAR

Explanation

This data type is used for variable-length string data. While it's possible to store the GeoJSON as a text string in a VARCHAR column, this approach doesn't allow for use of geospatial functions on the data.

**Your answer is incorrect**

  

VARIANT

Explanation

VARIANT is a flexible data type in Snowflake that can store semi-structured data, including JSON. Storing GeoJSON in a VARIANT column preserves its structure, but Snowflake's geospatial functions are designed to operate on GEOGRAPHY or GEOMETRY data types, not directly on VARIANT data.

**Correct answer**

  

GEOGRAPHY

Explanation

This data type is specifically designed for storing geospatial data that represents features on the Earth's surface using a spherical coordinate system (WGS 84 standard). It supports various geospatial formats, including GeoJSON, and allows for accurate spatial operations and analyses.

  

  

Overall explanation

When working with geospatial data that represents real-world locations using standard longitude and latitude coordinates, the GEOGRAPHY data type is the most appropriate choice. It adheres to the WGS 84 standard coordinate system, and supports various geospatial formats, including GeoJSON.

By storing GeoJSON data in a GEOGRAPHY column, you can use Snowflake's built-in geospatial functions to perform spatial analyses, such as calculating distances, finding intersections, and more. 

To store the provided GeoJSON data in a Snowflake table with a GEOGRAPHY column: 

CREATE TABLE geospatial_data (

id INT,

location GEOGRAPHY

);

INSERT INTO geospatial_data (id, location)

VALUES (1, TO_GEOGRAPHY('{

"type": "Point",

"coordinates": [-122.4194, 37.7749]

}'));

  

Question 45

Incorrect

Which function is used to return the name of the organization to which the current account belongs?

Choose **one** correct answer.

  

  

Overall explanation

The context function CURRENT_ORGANIZATION_NAME() is used to return the name of the organization that owns the current Snowflake account. This is particularly useful in environments where an organization contains multiple accounts (e.g., dev, staging, prod) and administrators or automated scripts need to dynamically identify the organization context.

This function requires no arguments and returns a VARCHAR value containing the name of the organization. All roles have the privilege to execute this function. Here's an example of it in action:

- SELECT CURRENT_ORGANIZATION_NAME();

This will return a string such as:

- MY_ORGANIZATION

  

  

Question 48

Incorrect

Which two of the following statements are true regarding Snowflake resource monitors?

Choose **two** correct answers.

**Correct selection**

  

Defining trigger thresholds that are greater than 100% is allowed

Explanation

Snowflake explicitly permits defining trigger thresholds greater than 100% of the credit quota. This means a monitor could, for example, have an action at 120% of quota.

**Correct selection**

  

Resource monitors can define at most one SUSPEND_IMMEDIATE action

Explanation

A resource monitor can include at most one SUSPEND_IMMEDIATE trigger (and similarly one SUSPEND trigger) by design . You cannot have two separate immediate-suspend actions on the same monitor.

  

Resource monitors can define a maximum of 3 NOTIFY triggers

Explanation

Snowflake allows **up to 5** notify triggers on a single resource monitor : "[Each resource monitor supports up to a maximum of 5 NOTIFY action triggers.](https://docs.snowflake.com/en/sql-reference/sql/create-resource-monitor#usage-notes)"

**Your selection is incorrect**

  

Multiple resource monitors can be set at the account-level

Explanation

[An account can have only one account-level resource monitor that covers all warehouses](https://docs.snowflake.com/en/user-guide/resource-monitors#monitor-type) . You may create additional monitors for specific warehouses, but you cannot have two account-wide monitors active at the same time.

**Your selection is incorrect**

  

It is mandatory to define a trigger when creating a resource monitor

Explanation

As stated in the Snowflake documentation, "[Triggers are optional; however, at least one trigger must be added to a resource monitor before it can perform any actions.](https://docs.snowflake.com/en/sql-reference/sql/create-resource-monitor#usage-notes)"

Overall explanation

Resource monitors enforce credit usage limits via threshold-based triggers (also called actions) defined as a percentage of the credit quota. Here's an example from the Snowflake documentation defining three triggers, NOTIFY, SUSPEND & SUSPEND_IMMEDIATE:

- CREATE OR REPLACE RESOURCE MONITOR limiter
- WITH CREDIT_QUOTA = 5000
- TRIGGERS ON 75 PERCENT DO NOTIFY
- ON 100 PERCENT DO SUSPEND
- ON 110 PERCENT DO SUSPEND_IMMEDIATE;

At least one trigger must be defined for a monitor to take any action; if no triggers are set, the monitor will never suspend or alert .

Regarding which level resource monitors can be applied, resource monitors can operate at either the account level or the warehouse level:

  

In the diagram above, “Resource Monitor 1” is an account-level monitor (covering all warehouses in the account) and “Resource Monitor 2/3” are warehouse-level monitors each assigned to specific warehouse groups. Snowflake **allows only one** account-level resource monitor per account , but you can create multiple monitors for individual warehouses. Each warehouse can only be assigned to a single warehouse-level monitor at a time.

  

Question 49

Incorrect

Which of the following is **not** a valid FREQUENCY option when creating a Snowflake resource monitor schedule?

Choose **one** correct answer.

  

Daily

Explanation

This is a supported frequency. Setting FREQUENCY = DAILY will make the monitor reset usage every day .

**Correct answer**

  

Hourly

Explanation

This is **not** a supported frequency option, making it the correct answer. Snowflake does not allow an hourly reset for resource monitors , so “Hourly” is invalid in this context.

  

Yearly

Explanation

This is a valid frequency. You can configure a monitor to reset yearly (e.g., FREQUENCY = YEARLY) 

**Your answer is incorrect**

  

Never

Explanation

This is a valid option. FREQUENCY = NEVER means the monitor’s credit usage never automatically resets ; the monitor will track cumulative usage until it hits the quota (or until an end time or manual intervention).

  

  

Question 52

Incorrect

Which two sections of a Snowflake Scripting block are optional?

Choose **two** correct answers.

**Correct selection**

  

DECLARE

Explanation

The DECLARE section is optional. It is used for declaring variables, cursors, etc., but a block doesn’t need it if declarations aren't required .

  

BEGIN ... END

Explanation

The BEGIN...END section is the executable code and is always required in a Snowflake Scripting block.

**Correct selection**

  

EXCEPTION

Explanation

The EXCEPTION section is optional. It is only needed if you want to include exception handlers; otherwise you can leave it out.

**Your selection is incorrect**

  

FINALLY

Explanation

There is no “finally” section in Snowflake Scripting. Error handling is done in the EXCEPTION section, and no separate finally-block construct exists.

**Your selection is incorrect**

  

TRANSACTION

Explanation

There is no dedicated transaction section in a Snowflake Scripting block. Transactions are controlled by commands (e.g., BEGIN TRANSACTION, COMMIT) within the BEGIN...END section.

Overall explanation

Snowflake Scripting blocks can include up to three sections delimited by keywords: an optional DECLARE section, a required BEGIN ... END section (the executable code), and an optional EXCEPTION section for error handling . Here's the basic structure shown in the Snowflake documentation:

DECLARE

-- (variable declarations, cursor declarations, etc.) ...

BEGIN

-- (Snowflake Scripting and SQL statements) ...

EXCEPTION

-- (statements for handling exceptions) ...

END;

A simple block requires only the BEGIN and END keywords . The DECLARE section (for defining variables, cursors, etc.) and the EXCEPTION section (for handling errors) are optional .

  

Question 62

Incorrect

Which of the following stored procedures allows you to classify and automatically tag the columns of a specific table in Snowflake using SQL?

Choose **one** correct answer.

  

SYSTEM$CLASSIFY_COLUMN

Explanation

SYSTEM$CLASSIFY_COLUMN is not a valid in-built stored procedure in Snowflake.

**Correct answer**

  

SYSTEM$CLASSIFY

Explanation

This stored procedure classifies and automatically applies system-defined tags to the columns of a specified table. It allows options such as specifying the number of rows to sample and setting the recommended sensitive data classification system tag to each column.

**Your answer is incorrect**

  

SYSTEM$CLASSIFY_SCHEMA

Explanation

This procedure classifies and tags all tables within a schema, not a single table.

  

Overall explanation

To classify and automatically tag the columns of a specific table in Snowflake using SQL,  use the SYSTEM$CLASSIFY stored procedure. This procedure analyses the specified table and applies system-defined tags, such as SEMANTIC_CATEGORY and PRIVACY_CATEGORY, to its columns. For example:

CALL SYSTEM$CLASSIFY('hr.tables.empl_info', {'auto_tag': true});

This command classifies the empl_info table within the hr schema and automatically applies the appropriate tags to its columns.

  

Question 63

Incorrect

What is the effect of changing a Snowflake sequence's increment from a positive to a negative value (e.g., from 1 to -1)?

Choose **one** correct answer.

**Your answer is incorrect**

  

The sequence will continue generating unique values without any risk of duplication

Explanation

Changing the sign of the increment can lead to the reuse of previously generated values, risking duplication.

  

The sequence will reset, and previously generated values will be overwritten

Explanation

Snowflake sequences do not reset or overwrite previously generated values when the increment is changed. 

**Correct answer**

  

The sequence may generate duplicate values, as previously issued numbers could be reused

Explanation

Altering the increment from positive to negative (or vice versa) may result in the generation of values that have already been issued, leading to potential duplicates.

  

The sequence will automatically adjust all previously generated values to match the new increment direction

Explanation

Snowflake does not retroactively adjust previously generated sequence values when the increment direction is changed.

Overall explanation

Sequences are designed to generate unique numeric values, often used for surrogate keys or unique identifiers. Each sequence has an INCREMENT value that determines the step between successive values. By default, this is a positive integer, causing the sequence to generate ascending values. 

However, if you alter the sequence to have a negative increment (e.g., changing from INCREMENT = 1 to INCREMENT = -1), the sequence will begin generating descending values. This change can lead to the generation of values that have already been issued, especially if the sequence had previously generated ascending values. For example, if the sequence had produced values 1, 2, 3, changing the increment to -1 could result in the next values being 2, 1, leading to duplicates. 

To avoid potential duplication, it's crucial to design sequences with a consistent increment direction and avoid changing the sign of the increment after the sequence has been in use.

  

  

Question 67

Incorrect

What is the default port number used by SnowCD to test HTTPS connectivity to Snowflake endpoints?

Choose **one** correct answer.

**Correct answer**

  

443

Explanation

Snowflake services use port 443 for HTTPS communication. SnowCD tests endpoint connectivity on this port by default unless otherwise specified.

  

Overall explanation

When using SnowCD, one of its core checks is validating HTTPS-level connectivity to Snowflake endpoints listed in the allowlist. These endpoints are tested on port 443, the standard port for encrypted HTTPS traffic.

Here's an example of an allowlist entry:

{ "type": "STAGE", "host": "mybucket.s3.us-west-2.amazonaws.com", "port": 443 }

SnowCD connects to each host and port to confirm that your environment can reach Snowflake’s services securely. Ensuring that port 443 is open and routable is a key part of passing SnowCD diagnostics.

  

  

  

Question 68

Incorrect

Which two connection parameters can be used to execute SQL queries in SnowSQL?

Choose **two** correct answers.

**Correct selection**

  

--query

Explanation

The --query (or -q) option lets you specify a SQL query directly on the command line for immediate execution.

**Correct selection**

  

--filename

Explanation

The --filename (or -f) option is used to execute a batch of SQL statements stored in a file.o execute one or more SQL queries from a specified file.

**Your selection is incorrect**

  

--execute

Explanation

There is no --execute flag in SnowSQL. This is a common misconception based on other CLI tools.

**Your selection is incorrect**

  

--run

Explanation

--run is not a valid SnowSQL command-line flag.

  

--input

Explanation

SnowSQL does not use a flag called --input for reading from standard input.

Overall explanation

SnowSQL is a command-line client that supports multiple execution methods for running SQL against your Snowflake account:

- The --query option allows you to run inline SQL commands, ideal for short or single statements.

- snowsql --query "SELECT CURRENT_DATE;"  
      
    

- The --filename option lets you execute all SQL commands listed in a file, useful for scripts or batch jobs.

- snowsql --filename script.sql  
      
    

  

Question 75

Incorrect

A developer is creating a stored procedure in Snowflake that returns a welcome message as a string. Which keyword must be included in the **procedure definition** to specify the type of value it will return?

Choose **one** correct answer.

**Correct answer**

  

RETURNS

  

Explanation

RETURN is not used to determine the type of value a stored procedure returns in the create statement for a stored procedure. However, the data you return from within the code body of a Javascript procedure can be specified with the return keyword. For example: 

CREATE or replace PROCEDURE proc3()

RETURNS VARCHAR

LANGUAGE javascript

AS

$$

var rs = snowflake.execute( { sqlText: 

`INSERT INTO table1 ("column 1") 

SELECT 'value 1' AS "column 1" ;`

} );

return 'Done.';

$$;

  

Overall explanation

When defining a stored procedure in Snowflake that returns a value (like a message, count, or status), you need to declare the expected return type using the **RETURNS** keyword. Without this, your procedure won’t know what kind of data it's allowed to return.

This simple stored procedure returns a customized greeting as a STRING, and RETURNS STRING clearly communicates that to both the engine and any developer calling it:

CREATE OR REPLACE PROCEDURE say_hello(name STRING)

RETURNS STRING

LANGUAGE SQL

AS

$$

BEGIN

RETURN 'Hello, ' || name || '!';

END;

$$;

  

  

Question 84

Incorrect

A developer is configuring an HTTP client to download unstructured files from a Snowflake stage using the REST API. The output of which two file functions can be supplied directly to the GET request to retrieve these files?

Choose **two** correct answers.

**Correct selection**

  

BUILD_SCOPED_FILE_URL

Explanation

This function generates a secure, temporary scoped URL for accessing a staged file. It’s ideal for short-lived, user-specific access and is supported by the REST API.

**Correct selection**

  

BUILD_STAGE_FILE_URL

Explanation

This generates a permanent file URL (provided proper permissions exist) that can also be used in REST API GET requests to retrieve staged files.

  

Overall explanation

To download a file from a Snowflake stage using the REST API, your client must send either a scoped URL (from BUILD_SCOPED_FILE_URL) or a file URL (from BUILD_STAGE_FILE_URL) in a GET request to the /api/files/ endpoint. These URLs provide secure, direct access to files stored in Snowflake’s internal or external stages.

  

Question 89

Incorrect

In Snowflake, a **nested view** is a view that references another view (which may itself reference yet another view, and so on). What is the maximum number of nested view levels allowed in Snowflake?

Choose **one** correct answer.

**Your answer is incorrect**

  

10

Explanation

Snowflake allows deeper nesting than 10 levels.

**Correct answer**

  

20

  

Question 92

Incorrect

In Snowflake, which of the following are valid **states** that a virtual warehouse can be in?

Choose **three** correct answers.

**Your selection is correct**

  

RESIZING

Explanation

RESIZING occurs temporarily when Snowflake is adjusting the number of clusters or size for a warehouse.

  

PAUSED

Explanation

PAUSED is not a Snowflake warehouse state. The proper term for inactive is SUSPENDED.

**Your selection is correct**

  

SUSPENDED

Explanation

SUSPENDED means the warehouse is inactive and not billing for compute, but still exists.

  

STOPPED

Explanation

STOPPED is not a recognized Snowflake warehouse state.

**Correct selection**

  

STARTED

Explanation

The warehouse is active and running, ready to process queries.

**Your selection is incorrect**

  

SHUTDOWN

Explanation

SHUTDOWN is not an official Snowflake state. Warehouses suspend, they don’t "shut down."

Overall explanation

Snowflake reports virtual warehouse states as:

- **STARTED**: Warehouse is running and ready.  
    
- **SUSPENDED**: Warehouse is inactive and not using compute resources. This is important because it's in this state that the virtual warehouse does not consume Snowflake credits.  
    
- **RESIZING**: Warehouse is changing size or cluster count.  
    

Question 94

Incorrect

What is the maximum value that can be set for the QUERY_ACCELERATION_MAX_SCALE_FACTOR virtual warehouse parameter? 

Choose **one** correct answer.

**Your answer is incorrect**

  

10

Explanation

10 is a valid value, but it’s not the maximum.

  

50

Explanation

While 50 is within the accepted range, it is not the highest permissible value.

**Correct answer**

  

100

Explanation

100 is the **maximum value** you can set for QUERY_ACCELERATION_MAX_SCALE_FACTOR, allowing QAS to use up to 100x the warehouse’s compute resources.

  

Overall explanation

The QUERY_ACCELERATION_MAX_SCALE_FACTOR sets the maximum amount of compute resources the Query Acceleration Service (QAS) can use, as a multiplier of the warehouse size. The valid range is **0 to 100**, where:

- **0** removes the limit (as much as needed, if available).  
    
- **8** is the default.  
    
- **100** is the maximum allowed.  
    

Setting a higher scale factor can improve query performance by allowing more compute, but may also increase credit usage.

Here's how we'd set this parameter on a warehouse called my_wh:

- ALTER WAREHOUSE my_wh SET QUERY_ACCELERATION_MAX_SCALE_FACTOR = 12;

  

Question 95

Incorrect

In Snowsight, what is the **maximum** time range you can select when viewing the Warehouse Activity chart for a virtual warehouse?

Choose **one** correct answer.

  

1 hour

Explanation

While 1 hour is a selectable range, it is not the default view.

**Your answer is incorrect**

  

1 day

Explanation

This option is available for user selection, but it’s not the default.

**Correct answer**

  

2 weeks

Explanation

Snowsight allows up to a **2-week** range for monitoring warehouse activity.

  

2 months

Explanation

The chart does not currently support a 1-month time range.

Overall explanation

Snowsight’s Warehouse Activity chart provides visual insights into how busy a virtual warehouse has been, specifically, how many queries were running or queued over time. Users can choose a custom time window from 1 hour to 2 weeks.

The chart's time interval (e.g., per-minute or per-day) adjusts automatically based on the selected time range. This makes it handy for spotting usage trends, identifying under- or over-utilisation, and optimising cost or performance settings.

To access the chart, go to Admin → Warehouses → [Warehouse Name], and the Warehouse Activity section shows the usage history of 2 weeks as the max selectable range.

  

Question 99

Incorrect

A data engineer is monitoring query activity in Snowflake and notices a long-running query that is consuming excessive resources. The engineer decides to stop the execution using the query's ID. Which of the following system functions should be used to immediately stop that specific query?

Choose **one** correct answer.

**Correct answer**

  

SYSTEM$CANCEL_QUERY

  

**Overall explanation**

**The SYSTEM$CANCEL_QUERY('<query_id>') function allows us to stop a currently executing query using its unique query ID. It's especially useful for halting long-running or runaway queries without disrupting other user operations.**

**To cancel someone else’s query, your role must have:**

- OWNERSHIP on the user who ran the query, or  
    
- OPERATE or OWNERSHIP on the warehouse that’s running the query.  
    

**This stops the query with the given ID and returns a message confirming cancellation:**

- SELECT SYSTEM$CANCEL_QUERY('d5493e36-5e38-48c9-a47c-c476f2111ce5');

  

  

Question 43

Skipped

When creating a tag in Snowflake, which optional parameter allows you to restrict the string values that can be assigned to the tag?

Choose **one** correct answer.

  

DEFAULT_VALUES

Explanation

This parameter does not exist in the context of creating tags in Snowflake.

  

VALID_VALUES

Explanation

While the name suggests functionality related to restricting values, this is not a recognized parameter in Snowflake's CREATE TAG statement.

**Correct answer**

  

ALLOWED_VALUES

Explanation

This is the correct parameter used in the CREATE TAG statement to specify a list of permissible string values that can be assigned to the tag. In this example statement found in the Snowflake documentation we're creating a tag named cost_center with allowed values restricted to 'finance', 'engineering', and 'marketing':

CREATE TAG cost_center ALLOWED_VALUES 'finance', 'engineering', 'marketing';

  

  

Snow prod-core-questions-exam (https://www.udemy.com/course/snowflake-snowpro-core-certification-questions-exam/learn/quiz/6582651/result/1734095511?expanded=1734095511#content)

1. **COPY command**

**Simple transformations during a load**

**#snowflakecerts** 

Snowflake supports transforming data while loading it into a table using the COPY command. Options include:

- Column reordering
- Column omission
- Casts
- Truncating text strings that exceed the target column length

  

1. SHOW GRANTS, difference between [https://docs.snowflake.com/en/sql-reference/sql/show-grants](https://docs.snowflake.com/en/sql-reference/sql/show-grants)

  

- **SHOW** **GRANTS** **TO** **ROLE** **<**role_name**>; —** to view the current set of privileges and roles granted to a role
- **SHOW** **GRANTS** **ON ROLE** **<**role_name**>; —** to view ownership of a role
- **SHOW** **GRANTS** **OF ROLE** **<**role_name**>;** — Lists all users and roles to which the role has been granted
- **SHOW** **FUTURE GRANTS** **IN** **SCHEMA** sales**.public or database;**
- **SHOW GRANTS ON ACCOUNT; —**Lists all the account-level (i.e. global) privileges that have been granted to roles.
- **SHOW** **GRANTS** **ON** **DATABASE** sales; — List all privileges that have been granted on the sales database

  

  

1. Snowpipe Streaming, data refresh methods supported by AWS

- SQS 
- lambda (?) [https://community.snowflake.com/s/article/How-to-Use-Snowflake-with-AWS-Lambda](https://community.snowflake.com/s/article/How-to-Use-Snowflake-with-AWS-Lambda)

  

  

1. Performance - how to determine number of queries queued or max concurrency

    select *

    from table(information_schema.warehouse_load_history(date_range_start=>dateadd('day',-14,current_date()), date_range_end=>current_date()))

    where avg_running > 0.00;

  

2. Understanding [Client-Side Encryption](https://docs.snowflake.com/en/user-guide/security-encryption-end-to-end#client-side-encryption)  on AWS external stage

- Master_key
- Encryption_key

  

The client-side encryption protocol works as follows:

- The customer creates a secret [master key](https://csrc.nist.gov/glossary/term/master_key), which is shared with Snowflake.
- The client, which is provided by the cloud storage service, generates a random encryption key and encrypts the file before uploading it into cloud storage. The random encryption key, in turn, is encrypted with the customer’s master key.
- Both the encrypted file and the encrypted random key are uploaded to the cloud storage service. The encrypted random key is stored with the file’s metadata.

**Ingesting client-side encrypted data into Snowflake**

-- create encrypted stage

**create** **stage** encrypted_customer_stage

url**=**'[s3://customer-bucket/data/](s3://customer-bucket/data/)'

**credentials=(**AWS_KEY_ID**=**'ABCDEFGH' AWS_SECRET_KEY**=**'12345678'**)**

**encryption=(**MASTER_KEY**=**'eSxX...='**);**

  

-- create table and ingest data from stage

**CREATE** **TABLE** **users** **(**id **bigint,** **name** **varchar(**500**),** purchases **int);**

**COPY** **INTO** **users** **FROM** **@**encrypted_customer_stage**/users;**

  

or alternatively

-- Run the copy into command and provide the encryption key

copy into mytest from @MYS3STAGEROLE/testabc1.csv file_format=(TYPE=CSV)

encryption=(MASTER_KEY='8K9j/mzd05zGVBAmUAs1I1Oi4BsKEl0Yp8445jzi3I0=') ;

  

1. **Advantage of Configuring a Snowflake storage integration to access Amazon S3**

Storage Integrations are named, Snowflake objects that 

- avoid the need for passing explicit cloud provider credentials such as secret keys or access tokens, avoid supplying credentials when creating a stage or when loading or unloading data
- Integration objects store an AWS identity and access management (IAM) user ID
- Integration objects store the encryption master_key
- **STORAGE_ALLOWED_LOCATIONS = ('****_cloud_specific_url_****')**

- Explicitly limits external stages that use the integration to reference one or more storage locations (i.e. S3 bucket, GCS bucket, or Azure container). Supports a comma-separated list of URLs for existing buckets and, optionally, paths used to store data files for loading/unloading. Alternatively supports the * wildcard, meaning “allow access to all buckets and/or paths”.

  

  

Alternative option: **Configure an S3 bucket access policy** 

[**https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user**](https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user)

  

- **Creating an IAM policy**

  

- **create a stage using the IAM credentials**

**CREATE** **OR** **REPLACE** **STAGE** my_S3_stage

  URL**=**'[s3://mybucket/load/files/](s3://mybucket/load/files/)'

  **CREDENTIALS=(**AWS_KEY_ID**=**'1a2b3c' AWS_SECRET_KEY**=**'4x5y6z'**)**

  **ENCRYPTION=(TYPE=**'AWS_SSE_KMS' KMS_KEY_ID **=** 'aws/key'**)**

  

  

  

1. Options to reload failed files by COPY INTO 

- Specify the file name in COPY INTO command: COPY INTO FILMS FROM @FILM_STAGE/films.csv or COPY INTO FILMS FROM @FILM_STAGE

FILES = ('films.csv');

- or Alternatively use COPY INTO FILMS FROM @FILM_STAGE which will load all unloaded files

  

- **TYPE = CSV | JSON | AVRO | ORC | PARQUET | XML [ ... ]**

  

1. COPY INTO

- **VALIDATION_MODE** allows user to perform a dry-run of load process to expose errors. VALIDATION_MODE = [‘RETURN_n_ROWS’, ‘RETURN ERRORS’, ‘RETURN_ALL_ERRORS]

- COPY INTO A_TABLE FROM @A_STAGE VALIDATION__MODE = ‘RETURN_ERRORS’

- VALIDATION_MODE does not support COPY statements that transform data during a load. If the parameter is specified, the COPY statement returns an error.
- **VALIDATE** is a table function to view all errors encountered during a previous COPY INTO execution. 
- SELECT * FROM TABLE ( VALIDATE (A_TABLE, JOB_ID => ‘3674-3785-887T-587’));

  

9. KAFKA CONNECTOR

- Each Kafka message is passed to Snowflake in **JSON format or Avro** format.

  

1. STREAMS

- **METADATA$ACTION**

Indicates the DML operation (INSERT, DELETE) recorded.

- **METADATA$ISUPDATE**

Indicates whether the operation was part of an UPDATE statement. Updates to rows in the source object are represented as a pair of DELETE and INSERT records in the stream with a metadata column METADATA$ISUPDATE values set to TRUE.

Note that streams record the differences between two offsets. If a row is added and then updated in the current offset, the delta change is a new row. The METADATA$ISUPDATE row records a FALSE value.

- **METADATA$ROW_ID**

Specifies the unique and immutable ID for the row, which can be used to track changes to specific rows over time.

  

  

1. STREAMS

- A stream becomes stale when its offset is outside of the data retention period for its source table (or the underlying tables for a source view)
- If the data retention period for a table is **_less than 14 days_**, and a stream has not been consumed, Snowflake temporarily extends this period to prevent it from going stale. The period is extended to the stream’s offset, up to a maximum of 14 days by default, regardless of the [Snowflake edition](https://docs.snowflake.com/en/user-guide/intro-editions) for your account

DATA_RETENTION_TIME_IN_DAYS MAX_DATA_EXTENSION_TIME_IN_DAYS Consume Streams in X Days

14 0 14

1 14 14

0 90 90

- The MAX_DATA_EXTENSION_TIME_IN_DAYS parameter enables you to limit this automatic extension period to control storage costs for data retention or for compliance reasons.

  

  

1. Behaviours on CLONE

- Currently, when a database or schema that contains a stream and its source table (or the underlying tables for a source view) is cloned, any unconsumed records in the stream clone are inaccessible. This behavior is consistent with [Time Travel](https://docs.snowflake.com/en/user-guide/data-time-travel) for tables. If a table is cloned, historical data for the table clone begins at the time/point when the clone was created.

  

1. Change Tracking Options

- streams
- **CHANGES Clause: Read-only Alternative to Streams**

As an alternative to streams, Snowflake supports querying change tracking metadata for tables or views using the [CHANGES](https://docs.snowflake.com/en/sql-reference/constructs/changes) clause for SELECT statements. The CHANGES clause enables querying change tracking metadata between two points in time without having to create a stream with an explicit transactional offset. Using the CHANGES clause does **_not_** advance the offset (i.e. consume the records). Multiple queries can retrieve the change tracking metadata between different transactional start and endpoints. This option requires specifying a transactional start point for the metadata using an [AT | BEFORE](https://docs.snowflake.com/en/sql-reference/constructs/at-before) clause; the end point for the change tracking interval can be set using the optional END clause.

A stream stores the current transactional [table version](https://docs.snowflake.com/en/user-guide/streams-intro#label-streams-table-versioning) and is the appropriate source of CDC records in most scenarios. For infrequent scenarios that require managing the offset for arbitrary periods of time, the CHANGES clause is available for your use.

Currently, the following must be true before change tracking metadata is recorded:

**Tables**

Either enable change tracking on the table (using [ALTER TABLE](https://docs.snowflake.com/en/sql-reference/sql/alter-table) … CHANGE_TRACKING = TRUE), or create a stream on the table (using [CREATE STREAM](https://docs.snowflake.com/en/sql-reference/sql/create-stream)).

  

1. JSON NULL impacting query performance

- JSON NULL is different from SQL NULL. JSON null is those element values are ‘null’ which is still a string that will prevent the elements from being extracted, SQL null is an empty value. As a result, JSON with a ‘null’ value will have a query performance impact.

  

  

1. Querying metadata for staging file

**Metadata Columns**

Currently, the following metadata columns can be queried or copied into tables:

- **METADATA$FILENAME**

Name of the staged data file the current row belongs to. Includes the path to the data file in the stage.

- **METADATA$FILE_ROW_NUMBER**

Row number for each record in the staged data file.

- **METADATA$FILE_CONTENT_KEY**

Checksum of the staged data file the current row belongs to.

- **METADATA$FILE_LAST_MODIFIED**

Last modified timestamp of the staged data file the current row belongs to. Returned as TIMESTAMP_NTZ.

- **METADATA$START_SCAN_TIME**

Start timestamp of operation for each record in the staged data file. Returned as TIMESTAMP_LTZ.

  

1. File Unloading

**Output Data File Details**

The following table describes the general details for the output files generated by Snowflake when unloading data:

Feature Supported Notes

- Location of files Local files Files are first unloaded to a Snowflake internal location, then can be downloaded locally using [GET](https://docs.snowflake.com/en/sql-reference/sql/get).

Files in Amazon S3 Files can be unloaded directly to any user-supplied bucket in S3, then can be downloaded locally using AWS utilities.

Files in Google Cloud Storage Files can be unloaded directly to any user-supplied container in Cloud Storage, then can be downloaded locally using Cloud Storage utilities.

Files in Microsoft Azure Files can be unloaded directly to any user-supplied container in Azure, then can be downloaded locally using Azure utilities.

- File formats

Delimited files (CSV, TSV, etc.) Any valid delimiter is supported; default is comma (i.e. CSV).

JSON

Parquet

- File encoding UTF-8 Output files are always encoded using UTF-8, regardless of the file format; no other character sets are supported.

  

1. Share, MANAGING GRANTS

- **Option 1:** Grant privileges on objects to a share via a database role.

- Segment the securable objects in a share by creating multiple database roles in a database to a share. Grant privileges on a subset of the objects in the database to each database role. Then grant each database role to the share.
- After creating a database from a share that includes database roles, data consumers grant each shared database role to one or more [account roles](https://docs.snowflake.com/en/user-guide/security-access-control-overview.html#label-access-control-overview-role-types) in their own account.
- Note: A shared database role does not support future grants on objects. For details, see [GRANT DATABASE ROLE … TO SHARE](https://docs.snowflake.com/en/sql-reference/sql/grant-database-role-share).

- **Option 2:** Grant privileges on objects directly to a share.

  

1. STAGE privileges

For stages:

- USAGE only applies to external stages.
- READ | WRITE only applies to internal stages. In addition, to grant the WRITE privilege on an internal stage, the READ privilege must first be granted on the stage.

  

1. DEFAULT_SECONDARY_ROLE

- **DEFAULT_SECONDARY_ROLES = ( 'ALL' )**

Specifies the set of secondary roles that are active for the user’s session upon login. Secondary roles are a set of roles that authorize any SQL action **_other than_** the execution of CREATE _<object>_ statements. The permissions to perform these actions can be granted to the primary role, secondary roles, or any lower roles in the role hierarchies.

Note that specifying a default secondary role for a user does **_not_** grant the role to the user. The role must also be granted explicitly to the user using the GRANT ROLE command.

The following values are supported:

**ALL:**

All roles that have been granted to the user.

Note that the set of roles is reevaluated when each SQL statement executes. If additional roles are granted to the user, and that user executes a new SQL statement, the newly granted roles are active secondary roles for the new SQL statement. The same logic applies to roles that are revoked from a user.

Default: NULL

  

1. DATABASE ROLE

- Grant privileges on a subset of the objects in the database to each database role. Then grant each database role to other roles or databases roles

  

  

1. Clone

- A cloned object does not retain the privileges of the source object, with the exception of tables
- Internal named stages and external tables are never cloned. Cloning database/schema containing Internal name stage and external table , will result in an error
- A cloned table does not contain the load history of the source table

  

1. Replication

- A replicated object does not retain the privileges of the source object

3. a user with org admin role can setup replication
4. external tables, event tables, temporary stages and class instances are not replicated

  

5. Secure Data Sharing

A share can contain the following types objects

- One database
- table
- external table
- secure view
- secure materialised view
- secure function
- Data consumer Accounts

  

Certain behaviours

- **database objects added to a share become immediately available to all consumers.**
- new objects added to the shared database will not be available to consumers, need to explicit add a grant to a share to make it available to consumers
- only one database can be added per share
- future grants cannot be used in shares
- Share is only applicable within the same region and cloud provider
- Sharing is not available on the VPS edition 
- No limit on number of consumer accounts, or number of shares
- Only user with account admin role or create share privileges can create share
- **Time travel is not avail on shared objects. Data retention disabled for a database created from a share, I.E. DATA_RETENTION_TIME_IN_DAYS = 0**
- A data consumer cannot create a clone of the shared database or database objects
- A shared database object is read only, cannot be reshared, or cloned or replicated
- A data consumer cannot create objects in a shared database
- To create a database from a share a user must have the IMPORT SHARE privileges

  

Read account — Managed Account

  

Data exchange

- The VPS version of Snowflake cannot leverage data exchange

  

1. Context Parameters

General Context

[CURRENT_CLIENT](https://docs.snowflake.com/en/sql-reference/functions/current_client)

[CURRENT_DATE](https://docs.snowflake.com/en/sql-reference/functions/current_date)

[CURRENT_IP_ADDRESS](https://docs.snowflake.com/en/sql-reference/functions/current_ip_address)

[CURRENT_REGION](https://docs.snowflake.com/en/sql-reference/functions/current_region)

CURRENT_SESSION

  

1. Performance

  

Multi-cluster Warehouses

  

  

- Scaling up can only be done manually.

  

- For a Warehouse size = L, how many credits it’s going to consume in 4 hours? 32 credits

  

- X-Small  Small Medium Large X-Large 2X-Large 3X-Large 
- 1 2 4 8 16 32 64 128

  

1. Multi-column clustering key

- Cluster columns that are most actively used in selective filters. If there is room for additional cluster keys, then consider columns frequently used in join predicates
- If you are defining a multi-column clustering key for a table, the order in which the columns are specified in the CLUSTER BY clause is important. As a general rule, Snowflake recommends ordering the columns from **_lowest_** cardinality to **_highest_** cardinality. Putting a higher cardinality column before a lower cardinality column will generally reduce the effectiveness of clustering on the latter column.
- A column with very low cardinality might yield only minimal pruning, such as a column named IS_NEW_CUSTOMER that contains only Boolean values. At the other extreme, a column with very high cardinality is also typically **_not_** a good candidate to use as a clustering key directly. For example, a column that contains nanosecond timestamp values would not make a good clustering key.

  

1. Query profile

- Spilling to local disk
- Spilling to remote disk
- Group by on a column with high cardinality or sort a large number of rows - causing spilling to disk

  

1. Caching

- Services layer: metadata cache, result cache (24 hour cache/31 days reset) - in memory, across virtual warehouses
- Virtual Warehouse: local disk cache - SSD cache, warehouse cache, raw data cache, will be cleared out if the virtual warehouse is suspended
- Storage layer: remote disk

**Snowflake Cache Layers**

The diagram below illustrates the levels at which data and results are cached for subsequent use. These are:-

- **Result Cache:**  Which holds the results of every query executed in the past 24 hours. These are available across virtual warehouses, so query results returned to one user is available to any other user on the system who executes the same query, provided the underlying data has not changed.
- **Local Disk Cache:**  Which is used to cache data used by SQL queries.  Whenever data is needed for a given query it's retrieved from the _Remote Disk_ storage, and cached in SSD and memory.
- **Remote Disk:**  Which holds the long term storage.  

  

  

1. Example of CREATE TABLE … USING TEMPLATE

- USED IN CONJUNCTION WITH SELECT ARRAY_AGG(OBJECT_CONSTRUCTURE(*))
- the arguments come from table function INFER_SCHEMA

create table trips

using template (

    SELECT array_agg(object_construct(*))

  FROM TABLE(

    INFER_SCHEMA(

      LOCATION=>'@test_stage'

      , file_format => 'csv_format'

      )

    ));

  

  

**Questions from Udemy SNOWPRO CORE course**

  

  

1. Which object does an external function make use of to hold security related information?

- Answer: An **API integration** object stores information about an HTTPS proxy service,

- The cloud platform provider
- The type of proxy service
- the IDF and access credentials for a cloud platform role

- For a remote service to be called

- it must expose an HTTPS endpoint
- it must take JSON inputs and return JSON outputs

  

Snowflake supported languages for UDF

- Java
- Javascript
- Python
- SQL

External Function Limitations

- **Return Scalar value only**
- **External functions are Not sharable**
- **we can only write function, not stored procedure**

  

  

  

1. Notation of semi-structured data

- Dot notation: select src:employee.name from EMPLOYEES;
- BRACKET notation: select src[‘employee’][‘name’] from EMPLOYEES;

- Variant column names are case insensitive like all sql column name,
- Within each column the **data element names are case sensitive**

  

1. What’s the recommended compressed file size when loading data into Snowflake?

- 100-250MB

  

  

1. How many regions in a cloud platform can a Snowflake account be deployed into

- Answer: 1

  

1. How many database objects can a data provider add to a SHARE object:

- Answer: 1

  

**Questinos from Udemy Trial Test3 -** 

1. TASK_HISTORY

- This function can return all executions run in the past 7 days or the next scheduled execution within the next 8 days.
- This function returns a maximum of 10,000 rows, set in the RESULT_LIMIT argument value. The default value is 100
- RETURN TASKS WITH THE FOLLOWING STATUS:

- SCHEDULED: scheduled for execution.
- EXECUTING: currently executing.
- SUCCEEDED: execution successful.
- FAILED: execution failed.
- [FAILED_AND_AUTO_SUSPENDED](https://docs.snowflake.com/en/user-guide/tasks-intro.html#label-tasks-automatically-suspend): task failed, and was automatically suspended.
- CANCELLED: execution cancelled.
- SKIPPED

  

1. Snowpipe REST API - insertFiles end point

- The post can contain at most 5000 files.
- Each file path given must be <= 1024 bytes long when serialized as UTF-8.

1. Snowpipe REST API - insertReport api

- The 10,000 most recent events are retained.
- Events are retained for a maximum of 10 minutes.

  

1. Search Optimisation Limitation - search optimization service does not support the following:

- External tables.
- Dynamic tables.
- Materialized views.
- Columns defined with a [COLLATE clause](https://docs.snowflake.com/en/sql-reference/collation.html#label-collate-clause).
- Column concatenation.
- Analytical expressions.
- Casts on table columns (except for fixed-point numbers cast to strings).  
    Although search optimization supports predicates with implicit and explicit casts on constant values, it does not support predicates that cast values in the actual table column (except for casts from INTEGER and NUMBER to VARCHAR).
- GRANTS

To add, configure, or remove search optimization for a table, you must have the following privileges:

- You must have OWNERSHIP privilege on the table.
- You must have ADD SEARCH OPTIMIZATION privilege on the schema that contains the table.

  

1. Kafak connection - handling of files failed to load

- The Kafka connector moves files it could not load to the stage associated with the target table. The syntax for referencing a table stage is @[namespace.]%table_name.

  

  

1. A company is using a Snowflake account in Azure. The account has SAML SSO set up using ADFS as a SCIM identity provider. To validate Private Link connectivity, an Architect performed the following steps:

- Confirmed Private Link URLs are working by logging in with a username/password account
- Verified DNS resolution by running nslookups against Private Link URLs
- Validated connectivity using SnowCD
- Disabled public access using a network policy set to use the company’s IP address range
- Add the IP address into private link allowed list
- **Update the configuration of Azure AD SSO to include the private link URL**

  

1. API Integration

- for integration with External Function

- Required parameters: 

- api_provider, 
- api_aws_role_arn (Amazon Resource Name, acting as IAM role)
- api_allowed_prefixes
- proxy service - gateway

  

**Questinos from Udemy Trial Test2 -** 

  

1. Continuous data loading options

- Snowpipe with auto-ingest
- COPY command with a task

  

1. Stored Procedure: caller’s rights vs owner’s rights

- A stored procedure runs with either the caller’s rights or the owner’s rights. It cannot run with both at the same time. 
- The primary advantage of an owner’s rights stored procedure is that the owner can delegate specific administrative tasks, such as cleaning up old data, to another role without granting that role more general privileges, such as privileges to delete all data from a specific table.

  

1. Which of the following options is not a compression technique for AVRO file formats?

- BZ2
- Parque is not compatible with most compression techniques except AUTO & SNAPPY
- ALL OTHER FILE TYPES are compatible with most compression techniques except SNAPPY

  

1. Strong legal isolation & multi-tenancy

- MTT - if role level security is viable
- OPT - if row level security is not viable but RBAC is viable
- APT - if RBAC is not viable

  

1. KAFKA and Snowflake Kafka connector

- Kafka connector creates the following

- internal stage 
- pipe per topic partition
- table, if the table exists, the follow columns will be created,

- Snowflake table schema: contains two variant fields:

- RECORD_CONTENT - contains Kafka message
- RECORD_METADATA

  

  

1. How access policies can be applied to external tables

- An external table can be created with a row access policy, and the policy can be applied to the VALUE column
- A row access policy can be applied to a view created on top of an external table
- A row access policy cannot be directly added to a virtual column of an external table
- While clone a database, Snowflake clone the row access policy but NOT the external table
- Instead, create view with the virtual column and add row access policy to the view

  

1. Schema of the external table

all external tables include the following column:

- VALUE
- METADATA$FILENAME
- METADATA$FILE_ROW_NUMBER

  

  

1. Materialised view can be created on top of external table to improve the performance

  

2. A user can change object parameters using,

- ACCOUNTADMIN or user with PRIVILEGE

  

  

  

1. Using Snowpipe required privileges

  

  

2. TRANSACTIONS & DDL

- each DDL statement executes as a separate transaction, cannot be rolled back
- In  a BEGIN TRANSACTION… COMMIT block, if one statement fails, the rest of the completed statements are committed.
- IF DDL statement is executed while a transaction is active, the DDL statement

- implicitly commits the active transaction

  

  

1. GET_OBJECT_REFERENCES

- for listing objects referenced by a view
- create view jdemo_v as select * from jdemo2;
- select * from table(get_object_references(database_name=> 'test_db', schema_name=> 'public', object_name => 'jdemo_v'));
- Only returns referenced tables or views

  

1. **Modifying the COPY statement in a pipe definition**

Complete the following steps to modify the COPY statement in a pipe definition; for example, when columns are added to the target table.

To execute the commands in this section, the current role for the user must have the OWNERSHIP privilege on the pipe.

- Pause the pipe (using [ALTER PIPE … SET PIPE_EXECUTION_PAUSED=true](https://docs.snowflake.com/en/sql-reference/sql/alter-pipe)).
- Query the [SYSTEM$PIPE_STATUS](https://docs.snowflake.com/en/sql-reference/functions/system_pipe_status) function and verify that the pipe execution state is PAUSED and the pending file count is 0.
- Recreate the pipe to change the COPY statement in the definition. Choose **_either_** of the following options:
- Pause the pipe again.
- Review the configuration steps for your cloud messaging service to ensure the settings are still accurate:

  

- Resume the pipe (using ALTER PIPE … SET PIPE_EXECUTION_PAUSED = false).
- Query the SYSTEM$PIPE_STATUS function again and verify that the pipe execution state is RUNNING.

  

  

54. Replication cost

- Charges based on replication are divided into two categories: data transfer and compute resources. Both categories are billed on the target account
- the target account also incurs the following cost

- Standard storage costs
- costs in maintaining materialised views
- costs in maintaining search optimisation

  

1. ALTER TASK … SET SCHEDULE = ‘ÚSING CRON */3 * * * * UTC’;

  

2. Semi-structured and structured data functions

- STRIP_NULL_VALUE: converts a JSON NULL to SQL NULL.
- PARSE_JASON, TRY_PARSE_JASON returns a VARIANT
- TO_JASON returns a varcher
- OBJECT_CONSTRUCT: returns an object constructed from arguments, the arguments can be from a a table or from a set of values

  

1. COPY_HISTORY

- The COPY_HISTORY command retains the loading history for both the COPY into command and Snowpipe **for the last** **14** **days**.
- You can execute it by running: select * from table(information_schema.copy_history())

  

**LOAD_HISTORY VIEW IN INFORMATION_SCHEMA view** 

- enables you to retrieve the history of data loaded into tables using the [COPY INTO <table>](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table) command **within the last 14 days**

- This view does not return the history of data loaded using Snowpipe
- This view returns an upper limit of 10,000 rows

Alternative without 10,000 rows limit

[LOAD_HISTORY view](https://docs.snowflake.com/en/sql-reference/account-usage/load_history) (Account Usage), 

[COPY_HISTORY function](https://docs.snowflake.com/en/sql-reference/functions/copy_history) (Information Schema), This table function can be used to query Snowflake data loading history along various dimensions within the last 14 days, The table function avoids the 10,000 row limitation of the [LOAD_HISTORY View](https://docs.snowflake.com/en/sql-reference/info-schema/load_history). The results can be filtered using SQL predicates.

[COPY_HISTORY view](https://docs.snowflake.com/en/sql-reference/account-usage/copy_history) (Account Usage).

  

INFORMATION_SCHEMA VIEW ACCOUNT_USAGE VIEWS

LOAD_HISTORY VIEW COPY_HISTORY VIEW

LOAD_HISTORY VIEW

  

INFORMATION_SCHEMA table function

COPY_HISTORY

  

68.**STATEMENT_TIMEOUT_IN_SECONDS**

- By Default: 172800 (i.e. 2 days)
- Value: 0 to 604800 (i.e. 7 days) — a value of 0 specifies that the maximum timeout value is enforced
- Max: 7 days

  

1. **STATEMENT_QUEUED_TIMEOUT_IN_SECONDS**

- Value: 0 to any value,
- Default: 0 (no timeout)

  

1. ALTER ACCOUNT SET PERIODIC_DATA_REKEYING = true;

- Required Enterprise edition

  

1. Materialised views and clustering

- You can cluster [materialized views](https://docs.snowflake.com/en/user-guide/views-materialized), as well as tables. The rules for clustering tables and materialized views are generally the same. For a few additional tips specific to materialized views, see [Materialized Views and Clustering](https://docs.snowflake.com/en/user-guide/views-materialized.html#label-clustering-base-table-and-materialized-view) and [Best Practices for Materialized Views](https://docs.snowflake.com/en/user-guide/views-materialized.html#label-best-practices-for-materialized-views).
- An existing clustering key is copied when a table is created using CREATE TABLE … CLONE. However, Automatic Clustering is [suspended for the cloned table](https://docs.snowflake.com/en/user-guide/object-clone.html#label-cloning-and-clustering-keys) and must be resumed.

  

1. **Creating managed access schemas**[¶](https://docs.snowflake.com/en/user-guide/security-access-control-configure#creating-managed-access-schemas)

- Managed access schemas improve security by locking down privilege management on objects.
- With managed access schemas, object owners lose the ability to make grant decisions. Only the schema owner (i.e. the role with the OWNERSHIP privilege on the schema) or a role with the MANAGE GRANTS privilege can grant privileges on objects in the schema, including [future grants](https://docs.snowflake.com/en/user-guide/security-access-control-configure#label-granting-future-privs-on-schema-objects), centralizing privilege management.

  

  

  

  

  

  

  

1. Redirecting client connections

- Requires Business Criticl Edition or higher
- Client redirect is implemented through a Snowflake connection object, which stores a secure connection URL
- require replication setup between two accounts in difference regions, both accounts use the same <connection_name>
- <organization_name>-<connection_name>.[snowflakecomputing.com](http://snowflakecomputing.com)

  

1. Authentication and SSO

  

**Authentication best practices**

Snowflake recommends creating the method in the below priority order.

**Preference #1:** OAuth (either Snowflake OAuth or External OAuth)

**Preference #2:** External Browser, if it's a desktop application that doesn’t support OAuth

**Preference #3:** Okta native authentication, if you’re using Okta, and the app supports this method while not supporting OAuth or external browser authentication yet.

**Preference #4:** Key Pair Authentication, mostly used for service account users. Since this requires the client application to manage private keys, complement it with your internal key management software.

**Preference #5:** Password, this should be the last option for applications that don’t support any of the above options. This option is commonly used for service account users connecting from 3rd party ETL apps.

  

**Snowflake security**

  

Federated authenticaion & SSO

  

Snowflake supports **_most_** SAML 2.0-compliant vendors as an IdP; however, certain vendors include native support for Snowflake (see below for details).

**Supported identity providers**

The following vendors provide **_native_** Snowflake support for federated authentication and SSO:

- [Okta](http://www.okta.com/) — hosted service  
    
- [Microsoft AD FS](https://msdn.microsoft.com/en-us/library/bb897402.aspx) (Active Directory Federation Services) — on-premises software (installed on Windows Server)  
    

**Replicate the SSO Configuration**

Snowflake supports replication and failover/failback of the [SAML2 security integration](https://docs.snowflake.com/user-guide/admin-security-fed-auth-security-integration) from a source account to a target account.

For details, see [Replication of security integrations & network policies across multiple accounts](https://docs.snowflake.com/user-guide/account-replication-security-integrations).

  

**Key-pair authentication and key-pair rotation**

  

This authentication method requires, as a minimum, a 2048-bit RSA key pair.

  

**OAuth**

  

  

**Controlling network traffic with network policies**

  

Create network rules

  

1. Select the schema of the network rule. Network rule are schema-level objects.  
    

  

  

**ALTER** **NETWORK POLICY** my_policy **SET** **BLOCKED_NETWORK_RULE_LIST** **=** **(** 'other_network' **);**

**ALTER** **NETWORK POLICY** my_policy **ADD** **ALLOWED_NETWORK_RULE_LIST** **=** **(** 'new_rule' **);**

  

Activating Network Policy

  

- [Activate a network policy for your account](https://docs.snowflake.com/en/user-guide/network-policies#label-associating-network-policies-with-an-account)  
    
- [Activate network policies for individual users](https://docs.snowflake.com/en/user-guide/network-policies#label-associating-network-policies-user)  
    
- [Activate network policies for security integrations](https://docs.snowflake.com/en/user-guide/network-policies#label-associating-network-policies-integration)  
    

  

  

**Sharing** 

To facilitate performing this validation, Snowflake provides the [SIMULATED_DATA_SHARING_CONSUMER](https://docs.snowflake.com/en/sql-reference/parameters.html#label-simulated-data-sharing-consumer) session parameter.

At this time, the SIMULATED_DATA_SHARING_CONSUMER session parameter only supports secure views and secure materialized views, but does not support secure UDFs. Setting this parameter in a session enables you to simulate querying a secure view as a user in any of the consumer account(s) you plan to share the view with.

For example, for a consumer account named xy12345:

**ALTER** **SESSION** **SET** SIMULATED_DATA_SHARING_CONSUMER **=** xy12345**;**

  

  

1. **PREVENT_UNLOAD_TO_INLINE_URL**

**Type**

Account — Can be set only for Account

**Data Type**

Boolean

**Description**

Specifies whether to prevent ad hoc data unload operations to external cloud storage locations (i.e. [COPY INTO <location>](https://docs.snowflake.com/en/sql-reference/sql/copy-into-location) statements that specify the cloud storage URL and access settings directly in the statement). For an example, see [Unloading data from a table directly to files in an external location](https://docs.snowflake.com/en/sql-reference/sql/copy-into-location.html#label-copy-into-location-ad-hoc).

  

1. **Resource Optimisation: Performance**

  

- Data Ingest with Snowpipe and "Copy"

- "SNOWFLAKE"."ACCOUNT_USAGE"."COPY_HISTORY"
- CASE WHEN PIPE_NAME IS NULL THEN 'COPY' ELSE 'SNOWPIPE' END AS INGEST_METHOD
- With this high-level information you can determine if file sizes are too small or too big for optimal ingest. If you can map the volume to credit consumption you can determine which tables are consuming more credits per TB loaded.

  

- Scale Up vs. Out (Size vs. Multi-cluster)

- LIST OF WAREHOUSES AND DAYS WHERE MCW COULD HAVE HELPED
- SELECT TO_DATE(START_TIME) as DATE
- ,WAREHOUSE_NAME
- ,SUM(AVG_RUNNING) AS SUM_RUNNING
- ,SUM(AVG_QUEUED_LOAD) AS SUM_QUEUED
- FROM "SNOWFLAKE"."ACCOUNT_USAGE"."WAREHOUSE_LOAD_HISTORY"
- WHERE TO_DATE(START_TIME) >= DATEADD(month,-1,CURRENT_TIMESTAMP())
- GROUP BY 1,2
- HAVING SUM(AVG_QUEUED_LOAD) >0
- ;

  

**Screenshot**

  

  

- LIST OF WAREHOUSES AND QUERIES WHERE A LARGER WAREHOUSE WOULD HAVE HELPED WITH REMOTE SPILLING

- SELECT QUERY_ID
- ,USER_NAME
- ,WAREHOUSE_NAME
- ,WAREHOUSE_SIZE
- ,BYTES_SCANNED
- ,BYTES_SPILLED_TO_REMOTE_STORAGE
- ,BYTES_SPILLED_TO_REMOTE_STORAGE / BYTES_SCANNED AS SPILLING_READ_RATIO
- FROM "SNOWFLAKE"."ACCOUNT_USAGE"."QUERY_HISTORY"
- WHERE BYTES_SPILLED_TO_REMOTE_STORAGE > BYTES_SCANNED * 5  -- Each byte read was spilled 5x on average
- ORDER BY SPILLING_READ_RATIO DESC
- ;

  

- WAREHOUSE Cache Usage

- FROM "SNOWFLAKE"."ACCOUNT_USAGE"."QUERY_HISTORY"
-   
    

  

- Heavy Scanner - clustering is not enabled

- select 
-   User_name
- , warehouse_name
- , avg(case when partitions_total > 0 then partitions_scanned / partitions_total else 0 end) avg_pct_scanned
- from   snowflake.account_usage.query_history
- where  start_time::date > dateadd('days', -45, current_date)
- group by 1, 2
- order by 3 desc
- ;
- who are the users with the most (near) full table scans
- SELECT USER_NAME
- ,COUNT(*) as COUNT_OF_QUERIES
- FROM "SNOWFLAKE"."ACCOUNT_USAGE"."QUERY_HISTORY"
- WHERE START_TIME >= dateadd(month,-1,current_timestamp())
- AND PARTITIONS_SCANNED > (PARTITIONS_TOTAL*0.95)
- AND QUERY_TYPE NOT LIKE 'CREATE%'
- group by 1
- order by 2 desc;
-   
    

- AutoClustering History & 7-Day Average

- Average daily credits consumed by Auto-Clustering grouped by week over the last year.

- WITH CREDITS_BY_DAY AS (
- SELECT TO_DATE(START_TIME) as DATE
- ,SUM(CREDITS_USED) as CREDITS_USED
- FROM "SNOWFLAKE"."ACCOUNT_USAGE"."AUTOMATIC_CLUSTERING_HISTORY"
- WHERE START_TIME >= dateadd(year,-1,current_timestamp()) 
- GROUP BY 1
- ORDER BY 2 DESC 
-   )

- SELECT DATE_TRUNC('week',DATE)
- ,AVG(CREDITS_USED) as AVG_DAILY_CREDITS
- FROM CREDITS_BY_DAY
- GROUP BY 1
- ORDER BY 1
- ;

  

- Average daily credits consumed by Materialized Views grouped by week over the last year.

- "SNOWFLAKE"."ACCOUNT_USAGE"."MATERIALIZED_VIEW_REFRESH_HISTORY"

  

  

- Search Optimization History & 7-Day Average 

- "SNOWFLAKE"."ACCOUNT_USAGE"."SEARCH_OPTIMIZATION_HISTORY"

  

- Snowpipe History & 7-Day Average

- "SNOWFLAKE"."ACCOUNT_USAGE"."PIPE_USAGE_HISTORY"

  

- Replication History & 7-Day Average

- "SNOWFLAKE"."ACCOUNT_USAGE"."REPLICATION_USAGE_HISTORY"

  

- Credit Consumption by Warehouse

- ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY

  

- Average Query Volume by Hour (Past 7 Days) 

- SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY

  

- Warehouse Utilization Over 7 Day Average

- SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY

  

- STORAGE COSTS

- SNOWFLAKE.ACCOUNT_USAGE.STORAGE_USAGE

  

- COMPUTE FROM WAREHOUSES

- SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY

  

- Idle Users

- SELECT 
- *
- FROM SNOWFLAKE.ACCOUNT_USAGE.USERS 
- WHERE LAST_SUCCESS_LOGIN < DATEADD(month, -1, CURRENT_TIMESTAMP()) 
- AND DELETED_ON IS NULL;

  

- Set Statement Timeouts

- SHOW PARAMETERS LIKE 'STATEMENT_TIMEOUT_IN_SECONDS' IN ACCOUNT;
- SHOW PARAMETERS LIKE 'STATEMENT_TIMEOUT_IN_SECONDS' IN WAREHOUSE <warehouse-name>;
- SHOW PARAMETERS LIKE 'STATEMENT_TIMEOUT_IN_SECONDS' IN USER <username>;

  

  

- Stale Table Streams 

- Indicates whether the offset for the stream is positioned at a point earlier than the data retention period for the table (or 14 days, whichever period is longer). Change data capture (CDC) activity cannot be returned for the table.

  

- SHOW STREAMS;

  

- select * 
- from table(result_scan(last_query_id())) 
- where "stale" = true;

  

- Failed Tasks

- select *
-   from snowflake.account_usage.task_history
-   WHERE STATE = 'FAILED'
-   and query_start_time >= DATEADD (day, -7, CURRENT_TIMESTAMP())
-   order by query_start_time DESC
-   ;

  

- Long running tasks

- select DATEDIFF(seconds, QUERY_START_TIME,COMPLETED_TIME) as DURATION_SECONDS
-                 ,*
- from snowflake.account_usage.task_history
- WHERE STATE = 'SUCCEEDED'
- and query_start_time >= DATEADD (day, -7, CURRENT_TIMESTAMP())
- order by DURATION_SECONDS desc
-   ;

  

  

1. Create Azure private link

  

- Snowflake Business Critical Edition (or higher) deployed in Azure   
    
- ACCOUNTADMIN access in your Snowflake account   
    
- A resource group in Azure to work with 
- The ability to create/modify the following objects inside the Azure resource group:   
    

- Virtual network   
    
- Private endpoint   
    
- Private DNS zone (if routing traffic from inside your network)   
    

- Azure CLI access   
    

  

1. To validate Private Link Connectivity

- Confirm Private link URLs are working by logging in with username/password
- Verify DNS resolution by running nslookups against Private Link URLs
- SnowCD to validate connectivity
- Disable public access using a network policy set to use the company’s IP range
- Add the company’s IP range to the allowed list in the network policy
- **Update the configuration of the Azure AD SSO to use the Private Link URL**s