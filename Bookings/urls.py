from django.urls import path
from . import views

# "/" are put at the end of url name not in front
urlpatterns = [
    # path('',views.bookTable,name="bookTable"),
    path('',views.index,name="index"),
    path('bookTable/',views.bookTable,name="bookTable"),
    path('TableRecords/bookTable/',views.bookTable,name="bookTable"),
    path('TableRecords/',views.TableRecords,name="TableRecords"),
    path('bookTable/TableRecords/',views.TableRecords,name="TableRecords"),
    path('bookTable/reserveTable/',views.reserveTable,name="reserveTable"),
    path('TableRecords/bookTable/reserveTable/',views.reserveTable,name="reserveTable"),
    path('TableRecords/Unbook/<int:BookingID>',views.unbook, name='unbook'),
    path('bookTable/TableRecords/Unbook/<int:BookingID>',views.unbook, name='unbook'),
    path('updateBooking/<int:BookingID>',views.updateBooking, name='updateBooking'),
    path('TableRecords/updateBooking/<int:BookingID>',views.updateBooking, name='updateBooking'),
    path('bookTable/TableRecords/updateBooking/<int:BookingID>',views.updateBooking, name='updateBooking'),
    path('updateBooking/saveUpdate/<int:BookingID>',views.saveUpdate, name='saveUpdate'),
    path('bookTable/TableRecords/updateBooking/saveUpdate/<int:BookingID>',views.saveUpdate, name='saveUpdate'),
    path('TableRecords/updateBooking/saveUpdate/<int:BookingID>',views.saveUpdate, name='saveUpdate'),
]