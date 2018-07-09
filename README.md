# Getting started

The Akeneo API brought to you!

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=AKK-BLF-PIM%202.3-Python)


## How to Use

The following section explains how to use the Akkblfpim23 SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=AKK-BLF-PIM%202.3-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=AKK-BLF-PIM%202.3-Python&projectName=akkblfpim23)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=AKK-BLF-PIM%202.3-Python&projectName=akkblfpim23)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=AKK-BLF-PIM%202.3-Python&projectName=akkblfpim23)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from akkblfpim23.akkblfpim_23_client import Akkblfpim23Client
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=AKK-BLF-PIM%202.3-Python&libraryName=akkblfpim23.akkblfpim_23_client&projectName=akkblfpim23&className=Akkblfpim23Client)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=AKK-BLF-PIM%202.3-Python&libraryName=akkblfpim23.akkblfpim_23_client&projectName=akkblfpim23&className=Akkblfpim23Client)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| o_auth_access_token | OAuth 2.0 Access Token |



API client can be initialized as following.

```python
# Configuration parameters and credentials
o_auth_access_token = 'o_auth_access_token' # OAuth 2.0 Access Token

client = Akkblfpim23Client(o_auth_access_token)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [ProductController](#product_controller)
* [AttributeController](#attribute_controller)
* [AttributeOptionController](#attribute_option_controller)
* [AttributeGroupsController](#attribute_groups_controller)
* [CategoryController](#category_controller)
* [ChannelController](#channel_controller)
* [CurrencyController](#currency_controller)
* [FamilyController](#family_controller)
* [FamilyVariant2XOnlyController](#family_variant2_x_only_controller)
* [MeasureFamily2XOnlyController](#measure_family2_x_only_controller)
* [MiscController](#misc_controller)

## <a name="product_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ProductController") ProductController

### Get controller instance

An instance of the ``` ProductController ``` class can be accessed from the API Client.

```python
 product_controller = client.product
```

### <a name="get_product"></a>![Method: ](https://apidocs.io/img/method.png ".ProductController.get_product") get_product

> Assuming that the given identifier is the identifier of an existing product

```python
def get_product(self)
```

#### Example Usage

```python

product_controller.get_product()

```


### <a name="get_products"></a>![Method: ](https://apidocs.io/img/method.png ".ProductController.get_products") get_products

> TODO: Add a method description

```python
def get_products(self,
                     content_type,
                     cookie)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| contentType |  ``` Required ```  | TODO: Add a parameter description |
| cookie |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
content_type = 'application/json'
cookie = 'Cookie'

product_controller.get_products(content_type, cookie)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="attribute_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AttributeController") AttributeController

### Get controller instance

An instance of the ``` AttributeController ``` class can be accessed from the API Client.

```python
 attribute_controller = client.attribute
```

### <a name="get_attribute"></a>![Method: ](https://apidocs.io/img/method.png ".AttributeController.get_attribute") get_attribute

> Assuming that the given code is the code of an existing attribute

```python
def get_attribute(self)
```

#### Example Usage

```python

attribute_controller.get_attribute()

```


### <a name="get_attributes"></a>![Method: ](https://apidocs.io/img/method.png ".AttributeController.get_attributes") get_attributes

> TODO: Add Description

```python
def get_attributes(self)
```

#### Example Usage

```python

attribute_controller.get_attributes()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="attribute_option_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AttributeOptionController") AttributeOptionController

### Get controller instance

An instance of the ``` AttributeOptionController ``` class can be accessed from the API Client.

```python
 attribute_option_controller = client.attribute_option
```

### <a name="get_attribute_option"></a>![Method: ](https://apidocs.io/img/method.png ".AttributeOptionController.get_attribute_option") get_attribute_option

> Assuming that the given codes are respectively the code of an existing attribute and an existing option of this attribute

```python
def get_attribute_option(self)
```

#### Example Usage

```python

attribute_option_controller.get_attribute_option()

```


### <a name="get_attribute_options"></a>![Method: ](https://apidocs.io/img/method.png ".AttributeOptionController.get_attribute_options") get_attribute_options

> TODO: Add Description

```python
def get_attribute_options(self)
```

#### Example Usage

```python

attribute_option_controller.get_attribute_options()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="attribute_groups_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AttributeGroupsController") AttributeGroupsController

### Get controller instance

An instance of the ``` AttributeGroupsController ``` class can be accessed from the API Client.

```python
 attribute_groups_controller = client.attribute_groups
```

### <a name="get_attribute_group_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".AttributeGroupsController.get_attribute_group_2_x_only") get_attribute_group_2_x_only

> Assuming that the given code is the code of an existing attribute group

```python
def get_attribute_group_2_x_only(self)
```

#### Example Usage

```python

attribute_groups_controller.get_attribute_group_2_x_only()

```


### <a name="get_attribute_groups_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".AttributeGroupsController.get_attribute_groups_2_x_only") get_attribute_groups_2_x_only

> TODO: Add Description

```python
def get_attribute_groups_2_x_only(self)
```

#### Example Usage

```python

attribute_groups_controller.get_attribute_groups_2_x_only()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="category_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CategoryController") CategoryController

### Get controller instance

An instance of the ``` CategoryController ``` class can be accessed from the API Client.

```python
 category_controller = client.category
```

### <a name="get_category"></a>![Method: ](https://apidocs.io/img/method.png ".CategoryController.get_category") get_category

> Assuming that the given code is the code of an existing category

```python
def get_category(self)
```

#### Example Usage

```python

category_controller.get_category()

```


### <a name="get_categories"></a>![Method: ](https://apidocs.io/img/method.png ".CategoryController.get_categories") get_categories

> TODO: Add Description

```python
def get_categories(self)
```

#### Example Usage

```python

category_controller.get_categories()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="channel_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ChannelController") ChannelController

### Get controller instance

An instance of the ``` ChannelController ``` class can be accessed from the API Client.

```python
 channel_controller = client.channel
```

### <a name="get_channel"></a>![Method: ](https://apidocs.io/img/method.png ".ChannelController.get_channel") get_channel

> Assuming that the given code is the code of an existing channel

```python
def get_channel(self)
```

#### Example Usage

```python

channel_controller.get_channel()

```


### <a name="get_channels"></a>![Method: ](https://apidocs.io/img/method.png ".ChannelController.get_channels") get_channels

> TODO: Add Description

```python
def get_channels(self)
```

#### Example Usage

```python

channel_controller.get_channels()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="currency_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CurrencyController") CurrencyController

### Get controller instance

An instance of the ``` CurrencyController ``` class can be accessed from the API Client.

```python
 currency_controller = client.currency
```

### <a name="get_currency_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".CurrencyController.get_currency_2_x_only") get_currency_2_x_only

> Assuming that the given code is the code of an existing currency

```python
def get_currency_2_x_only(self)
```

#### Example Usage

```python

currency_controller.get_currency_2_x_only()

```


### <a name="get_currencies_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".CurrencyController.get_currencies_2_x_only") get_currencies_2_x_only

> TODO: Add Description

```python
def get_currencies_2_x_only(self)
```

#### Example Usage

```python

currency_controller.get_currencies_2_x_only()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="family_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FamilyController") FamilyController

### Get controller instance

An instance of the ``` FamilyController ``` class can be accessed from the API Client.

```python
 family_controller = client.family
```

### <a name="get_family"></a>![Method: ](https://apidocs.io/img/method.png ".FamilyController.get_family") get_family

> Assuming that the given code is the code of an existing family

```python
def get_family(self)
```

#### Example Usage

```python

family_controller.get_family()

```


### <a name="get_families"></a>![Method: ](https://apidocs.io/img/method.png ".FamilyController.get_families") get_families

> TODO: Add Description

```python
def get_families(self)
```

#### Example Usage

```python

family_controller.get_families()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="family_variant2_x_only_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FamilyVariant2XOnlyController") FamilyVariant2XOnlyController

### Get controller instance

An instance of the ``` FamilyVariant2XOnlyController ``` class can be accessed from the API Client.

```python
 family_variant_2_x_only_controller = client.family_variant_2_x_only
```

### <a name="get_family_variant_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".FamilyVariant2XOnlyController.get_family_variant_2_x_only") get_family_variant_2_x_only

> Assuming that the given codes are respectively the code of an existing family and an existing family variant

```python
def get_family_variant_2_x_only(self)
```

#### Example Usage

```python

family_variant_2_x_only_controller.get_family_variant_2_x_only()

```


### <a name="get_family_variants_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".FamilyVariant2XOnlyController.get_family_variants_2_x_only") get_family_variants_2_x_only

> TODO: Add Description

```python
def get_family_variants_2_x_only(self)
```

#### Example Usage

```python

family_variant_2_x_only_controller.get_family_variants_2_x_only()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="measure_family2_x_only_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MeasureFamily2XOnlyController") MeasureFamily2XOnlyController

### Get controller instance

An instance of the ``` MeasureFamily2XOnlyController ``` class can be accessed from the API Client.

```python
 measure_family_2_x_only_controller = client.measure_family_2_x_only
```

### <a name="get_measure_family_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".MeasureFamily2XOnlyController.get_measure_family_2_x_only") get_measure_family_2_x_only

> Assuming that the given code is the code of an existing measure family

```python
def get_measure_family_2_x_only(self)
```

#### Example Usage

```python

measure_family_2_x_only_controller.get_measure_family_2_x_only()

```


### <a name="get_measure_families_2_x_only"></a>![Method: ](https://apidocs.io/img/method.png ".MeasureFamily2XOnlyController.get_measure_families_2_x_only") get_measure_families_2_x_only

> TODO: Add Description

```python
def get_measure_families_2_x_only(self)
```

#### Example Usage

```python

measure_family_2_x_only_controller.get_measure_families_2_x_only()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="misc_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MiscController") MiscController

### Get controller instance

An instance of the ``` MiscController ``` class can be accessed from the API Client.

```python
 misc_controller = client.misc
```

### <a name="create_authentification_by_password"></a>![Method: ](https://apidocs.io/img/method.png ".MiscController.create_authentification_by_password") create_authentification_by_password

> TODO: Add Description

```python
def create_authentification_by_password(self,
                                            body,
                                            content_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |
| contentType |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body_value = "{\"username\":\"{{username}}\",\"password\":\"{{password}}\",\"grant_type\":\"password\"}"
body = json.loads(body_value)
content_type = 'application/json'

misc_controller.create_authentification_by_password(body, content_type)

```


### <a name="create_authentification_by_refresh_token"></a>![Method: ](https://apidocs.io/img/method.png ".MiscController.create_authentification_by_refresh_token") create_authentification_by_refresh_token

> TODO: Add Description

```python
def create_authentification_by_refresh_token(self,
                                                 body,
                                                 content_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |
| contentType |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body_value = "{\"refresh_token\":\"{{refreshToken}}\",\"grant_type\":\"refresh_token\"}"
body = json.loads(body_value)
content_type = 'application/json'

misc_controller.create_authentification_by_refresh_token(body, content_type)

```


[Back to List of Controllers](#list_of_controllers)



