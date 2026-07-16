# Django REST Framework (DRF)
---

## DRF Fundamentals

- [ ] 🔷 What is Django REST Framework?
- [ ] 🔷 Why DRF?
- [ ] 🔷 DRF Architecture
- [ ] 🔷 Request & Response Lifecycle
- [ ] 🔷 DRF Project Structure
- [ ] 🔷 Browsable API
- [ ] 🔷 APIView vs Django Views
- [ ] 🔷 DRF Components Overview

---

## Installation & Configuration

- [ ] 🔷 Installing DRF
- [ ] 🔷 Adding DRF to INSTALLED_APPS
- [ ] 🔷 DEFAULT_RENDERER_CLASSES
- [ ] 🔷 DEFAULT_PARSER_CLASSES
- [ ] 🔷 DEFAULT_AUTHENTICATION_CLASSES
- [ ] 🔷 DEFAULT_PERMISSION_CLASSES
- [ ] 🔷 DEFAULT_PAGINATION_CLASS
- [ ] 🔷 PAGE_SIZE
- [ ] 🔷 DEFAULT_FILTER_BACKENDS
- [ ] 🔷 Versioning Configuration

---

## API Views

- [ ] 🔷 APIView
- [ ] 🔷 Function-Based API Views
- [ ] 🔷 @api_view
- [ ] 🔷 GenericAPIView
- [ ] 🔷 ViewSets
- [ ] 🔷 ModelViewSet
- [ ] 🔷 ReadOnlyModelViewSet
- [ ] 🔷 Custom API Views
- [ ] 🔷 APIView Lifecycle
- [ ] 🟣 BaseAPIView Customization

---

## Generic Views

- [ ] 🔷 ListAPIView
- [ ] 🔷 RetrieveAPIView
- [ ] 🔷 CreateAPIView
- [ ] 🔷 UpdateAPIView
- [ ] 🔷 DestroyAPIView
- [ ] 🔷 ListCreateAPIView
- [ ] 🔷 RetrieveUpdateAPIView
- [ ] 🔷 RetrieveDestroyAPIView
- [ ] 🔷 RetrieveUpdateDestroyAPIView

---

## ViewSets

- [ ] 🔷 ViewSet
- [ ] 🔷 GenericViewSet
- [ ] 🔷 ModelViewSet
- [ ] 🔷 ReadOnlyModelViewSet
- [ ] 🔷 Router
- [ ] 🔷 DefaultRouter
- [ ] 🔷 SimpleRouter
- [ ] 🔷 basename
- [ ] 🔷 @action
- [ ] 🔷 Detail Actions
- [ ] 🔷 List Actions
- [ ] 🟣 Nested Routers

---

## Serializers

- [ ] 🔷 Serializer
- [ ] 🔷 ModelSerializer
- [ ] 🔷 Serializer Fields
- [ ] 🔷 Meta Class
- [ ] 🔷 Validation
- [ ] 🔷 Field Validation
- [ ] 🔷 Object Validation
- [ ] 🔷 Nested Serializer
- [ ] 🔷 SerializerMethodField
- [ ] 🔷 Read Only Fields
- [ ] 🔷 Write Only Fields
- [ ] 🔷 Extra Keyword Arguments
- [ ] 🔷 Partial Updates
- [ ] 🔷 create()
- [ ] 🔷 update()
- [ ] 🔷 save()
- [ ] 🔷 many=True
- [ ] 🟣 Dynamic Serializers
- [ ] 🟣 Writable Nested Serializers

---

## Serializer Fields

- [ ] 🔷 CharField
- [ ] 🔷 IntegerField
- [ ] 🔷 FloatField
- [ ] 🔷 DecimalField
- [ ] 🔷 BooleanField
- [ ] 🔷 DateField
- [ ] 🔷 DateTimeField
- [ ] 🔷 ChoiceField
- [ ] 🔷 EmailField
- [ ] 🔷 URLField
- [ ] 🔷 UUIDField
- [ ] 🔷 FileField
- [ ] 🔷 ImageField
- [ ] 🔷 PrimaryKeyRelatedField
- [ ] 🔷 SlugRelatedField
- [ ] 🔷 HyperlinkedRelatedField
- [ ] 🟣 Custom Serializer Fields

---

## Validation

- [ ] 🔷 validate()
- [ ] 🔷 validate_<field>()
- [ ] 🔷 Required Fields
- [ ] 🔷 Optional Fields
- [ ] 🔷 Custom Validators
- [ ] 🔷 UniqueValidator
- [ ] 🔷 ValidationError
- [ ] 🔷 Regex Validation
- [ ] 🟣 Reusable Validators

---

## Request & Response

- [ ] 🔷 Request Object
- [ ] 🔷 Response Object
- [ ] 🔷 status Module
- [ ] 🔷 JSON Response
- [ ] 🔷 Request Data
- [ ] 🔷 Query Parameters
- [ ] 🔷 Path Parameters
- [ ] 🔷 Headers
- [ ] 🔷 Cookies
- [ ] 🟣 Streaming Responses

---

## Authentication

- [ ] 🔷 Session Authentication
- [ ] 🔷 Basic Authentication
- [ ] 🔷 Token Authentication
- [ ] 🔷 JWT Authentication
- [ ] 🔷 Custom Authentication
- [ ] 🔷 Current User
- [ ] 🔷 Login API
- [ ] 🔷 Logout API
- [ ] 🔷 Refresh Token
- [ ] 🟣 OAuth2
- [ ] 🟣 Social Login

---

## Permissions

- [ ] 🔷 AllowAny
- [ ] 🔷 IsAuthenticated
- [ ] 🔷 IsAdminUser
- [ ] 🔷 IsAuthenticatedOrReadOnly
- [ ] 🔷 DjangoModelPermissions
- [ ] 🔷 DjangoObjectPermissions
- [ ] 🔷 Custom Permissions
- [ ] 🔷 Permission Classes
- [ ] 🟣 Object-Level Permissions

---

## Throttling

- [ ] 🔷 Anonymous Throttle
- [ ] 🔷 User Throttle
- [ ] 🔷 Scoped Throttle
- [ ] 🔷 Rate Configuration
- [ ] 🔷 Custom Throttles

---

## Parsers

- [ ] 🔷 JSONParser
- [ ] 🔷 FormParser
- [ ] 🔷 MultiPartParser
- [ ] 🔷 FileUploadParser
- [ ] 🟣 Custom Parsers

---

## Renderers

- [ ] 🔷 JSONRenderer
- [ ] 🔷 BrowsableAPIRenderer
- [ ] 🔷 TemplateHTMLRenderer
- [ ] 🟣 Custom Renderers

---

## Filtering

- [ ] 🔷 filter_backends
- [ ] 🔷 SearchFilter
- [ ] 🔷 OrderingFilter
- [ ] 🔷 DjangoFilterBackend
- [ ] 🔷 Custom Filtering
- [ ] 🟣 Complex Dynamic Filters

---

## Searching

- [ ] 🔷 search_fields
- [ ] 🔷 Multiple Search Fields
- [ ] 🔷 Exact Search
- [ ] 🔷 Partial Search
- [ ] 🟣 Full Text Search

---

## Ordering

- [ ] 🔷 ordering_fields
- [ ] 🔷 Default Ordering
- [ ] 🔷 Ascending Order
- [ ] 🔷 Descending Order

---

## Pagination

- [ ] 🔷 PageNumberPagination
- [ ] 🔷 LimitOffsetPagination
- [ ] 🔷 CursorPagination
- [ ] 🔷 Custom Pagination
- [ ] 🟣 Optimized Cursor Pagination

---

## File Uploads

- [ ] 🔷 File Upload APIs
- [ ] 🔷 Image Upload APIs
- [ ] 🔷 Multiple File Upload
- [ ] 🔷 File Validation
- [ ] 🟣 Chunked Uploads

---

## Relationships

- [ ] 🔷 Nested Relationships
- [ ] 🔷 ForeignKey Serialization
- [ ] 🔷 ManyToMany Serialization
- [ ] 🔷 Reverse Relationships
- [ ] 🔷 Hyperlinked Relationships
- [ ] 🟣 Recursive Relationships

---

## Exception Handling

- [ ] 🔷 APIException
- [ ] 🔷 ValidationError
- [ ] 🔷 ParseError
- [ ] 🔷 AuthenticationFailed
- [ ] 🔷 PermissionDenied
- [ ] 🔷 NotFound
- [ ] 🔷 Custom Exception Handler
- [ ] 🔷 Standard Error Response
- [ ] 🟣 Error Logging Middleware

---

## Versioning

- [ ] 🔷 URLPathVersioning
- [ ] 🔷 NamespaceVersioning
- [ ] 🔷 QueryParameterVersioning
- [ ] 🔷 HeaderVersioning
- [ ] 🟣 AcceptHeaderVersioning

---

## API Documentation

- [ ] 🔷 OpenAPI
- [ ] 🔷 Swagger
- [ ] 🔷 drf-yasg
- [ ] 🔷 drf-spectacular
- [ ] 🔷 API Schema
- [ ] 🔷 Examples
- [ ] 🔷 Tags
- [ ] 🟣 Custom Schema Generation

---

## Testing

- [ ] 🔷 APITestCase
- [ ] 🔷 APIClient
- [ ] 🔷 force_authenticate()
- [ ] 🔷 Authentication Testing
- [ ] 🔷 Serializer Testing
- [ ] 🔷 Permission Testing
- [ ] 🔷 API Integration Tests
- [ ] 🟣 Load Testing APIs

---

## Performance

- [ ] 🔷 select_related()
- [ ] 🔷 prefetch_related()
- [ ] 🔷 Query Optimization
- [ ] 🔷 Pagination Optimization
- [ ] 🔷 Serializer Optimization
- [ ] 🔷 Caching APIs
- [ ] 🔷 Redis Integration
- [ ] 🟣 Response Compression

---

## Security

- [ ] 🔷 JWT Security
- [ ] 🔷 CORS
- [ ] 🔷 CSRF
- [ ] 🔷 Rate Limiting
- [ ] 🔷 Secure File Uploads
- [ ] 🔷 Input Validation
- [ ] 🔷 Secret Management
- [ ] 🟣 API Key Authentication

---

## Deployment

- [ ] 🔷 Gunicorn
- [ ] 🔷 Nginx
- [ ] 🔷 Docker
- [ ] 🔷 Docker Compose
- [ ] 🔷 Environment Variables
- [ ] 🔷 HTTPS
- [ ] 🟣 Kubernetes

---

## DRF Best Practices

- [ ] 🔷 Fat Models, Thin Views
- [ ] 🔷 Service Layer
- [ ] 🔷 Repository Pattern
- [ ] 🔷 Serializer Separation
- [ ] 🔷 Consistent API Responses
- [ ] 🔷 API Versioning
- [ ] 🔷 Error Handling Strategy
- [ ] 🔷 Logging
- [ ] 🔷 Health Check Endpoint
- [ ] 🔷 API Documentation
- [ ] 🟣 Clean Architecture
- [ ] 🟣 Domain Driven Design (DDD)

---

## Useful DRF Ecosystem

- [ ] 🔷 drf-spectacular
- [ ] 🔷 drf-yasg
- [ ] 🔷 django-filter
- [ ] 🔷 djangorestframework-simplejwt
- [ ] 🔷 django-cors-headers
- [ ] 🔷 Pillow
- [ ] 🔷 Redis
- [ ] 🔷 Celery
- [ ] 🔷 WhiteNoise
- [ ] 🟣 drf-nested-routers
- [ ] 🟣 drf-flex-fields
- [ ] 🟣 drf-extensions
- [ ] 🟣 drf-api-key
