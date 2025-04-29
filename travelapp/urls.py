from django.urls import path
from travelapp import views
urlpatterns= [
    path("",views.index),
    path("about/",views.about),
    path("services/",views.services),
    path("details/",views.details),
    # path("pricing/",views.pricing),
    path("contact/",views.contact),
    path("register/",views.register),
    path("login/",views.login),
    path("logout/",views.logout),
    path("searching/",views.searching),
    path("special/",views.special),
    path("discount/",views.discount),
    path("order/",views.order),
    path("review/",views.review),
    path("bookings/",views.bookings),
    path("payment/",views.payment),
    path("reviewpage/",views.reviewpage),
    path("cancel/",views.cancel),
    




###############################################################################################################################################
############################################# ADMIN ###########################################################################################
    path("adminlogin/",views.admin_login),
    path("adminindex/",views.adminindex),

    # path("tourpack/",views.tourpack),
    # path("tourpacklist/",views.tourpacklist),

    path("packages/",views.packages),
    path("specialfield/",views.specialfield),
    path("addlocation/",views.addlocation),
    path("packagelist/",views.packagelist),
    path("specialfieldlist/",views.specialfieldlist),
    path("locationlist/",views.locationlist),

    # path("searchbooking/",views.searchbooking),
    path("booked/",views.booked),
    path("bookingcancel/",views.bookingcancel),
    path("reviewlist/",views.reviewlist),
    path("userlist/",views.userlist),
    path("userreject/",views.userreject),
    path("useraprove/",views.useraprove),
    path("admincate/",views.admincate),
    path("images/",views.images),
    path("imageslist/",views.imageslist),
    # path("imageslistupdate/",views.imageslistupdate),
    path("package_delete/",views.package_delete),
    path("update/",views.update),

    # path("bookings/",views.bookings),
    # path("servicepackages/",views.servicepackages),

    path("updatepkgimg/",views.updatepkgimg),
    path("deletepkgimg/",views.deletepkgimg),


    path("approvereview/",views.admin_approve_review),
    path("delete_review/",views.delete_review),
    
    




    





    ]