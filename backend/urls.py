from django.conf.urls import include, url
from django.contrib import admin
from hpcuiapi.controllers import FileController, ProjectController, UserController, ToolController, ToolFileController, WorkflowController
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^projects/$', ProjectController.ProjectsView.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/$', ProjectController.ProjectDetail.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/files/$', FileController.FilesView.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/tasks/$', WorkflowController.TasksView.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/task/(?P<uuid>[0-9a-z-]+)', WorkflowController.TaskView.as_view()),
    url(r'^file/(?P<fk>[0-9]+)/$', FileController.FileDetail.as_view()),
    url(r'^user/', UserController.UserView.as_view()),
    url(r'^ptools/$', WorkflowController.WorkflowToolsView.as_view()),
    url(r'^tools/$', ToolController.ToolsView.as_view()),
    url(r'^tools/(?P<fk>[0-9]+)/$', ToolController.ToolDetail.as_view()),
    url(r'^tools/(?P<tk>[0-9]+)/files/$', ToolFileController.ToolFilesView.as_view()),
    url(r'^tools/(?P<tk>[0-9]+)/files/(?P<fk>[0-9]+)/$', ToolFileController.ToolFilesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
