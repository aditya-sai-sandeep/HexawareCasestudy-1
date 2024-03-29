import hashlib

from dao.AdminService import AdminService
from dao.CustomerService import CustomerService
from dao.ReservationService import ReservationService
from dao.VehicleService import VehicleService


def custom_hash_password(password1):
    salt = "$2a$10$[}0w3rima-=-723%.;/'!87&*||]\]"
    password = password1
    combined_string = password + salt
    sha256 = hashlib.sha256()
    sha256.update(combined_string.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password
loop = True
table_creation = True
try:
    while loop:
        customerservice1 = CustomerService()
        vehicleservice1 = VehicleService()
        reservationservice1 = ReservationService()
        adminservice1 = AdminService()
        while table_creation:
            customerservice1.create_class()
            vehicleservice1.create_class()
            reservationservice1.create_table()
            adminservice1.create_class()
            table_creation= False

        print("Select table to ue functionalities")
        print("1.Customer\n2.Vehicle\n3.Reservation\n4.Admin\n5.Key Functionalities\n6.Exit")
        choice = int(input("enter your choice:"))

        if choice == 1:
            while True:
                print("1.Add Customer\t2.Update Customer\t3.Delete Customer\n4.Get Customer Details by ID\t5.Get "
                      "Customer Details by Name\t6.View All Customers\n7.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    customerservice1.RegisterCustomer()
                elif choice == 2:
                    customerservice1.UpdateCustomer()
                elif choice == 3:
                    customerservice1.DeleteCustomer()
                elif choice == 4:
                    customerservice1.GetCustomerById()
                elif choice == 5:
                    customerservice1.GetCustomerByUsername()
                elif choice == 6:
                    customerservice1.select()
                else:
                    break

        elif choice == 2:
            while True:
                print("1.Add Vehicle\t2.Update Vehicle\t3.Remove Vehicle\n4.Get Vehicle Details by ID\t5.View All "
                      "Vehicle\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    vehicleservice1.AddVehicle()
                elif choice == 2:
                    vehicleservice1.UpdateVehicle()
                elif choice == 3:
                    vehicleservice1.RemoveVehicle()
                elif choice == 4:
                    vehicleservice1.GetVehicleById()
                elif choice == 5:
                    vehicleservice1.GetAvailableVehicles()
                else:
                    break

        elif choice == 3:
            while True:
                print("1.Add Reservation\t2.Update Reservation\t3.Delete Reservation\n4.Get Reservation Details by "
                      "ID\t5.Get Reservation Details bu customer ID\t6.Get all reservations\n7.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    reservationservice1.CreateReservation()
                elif choice == 2:
                    reservationservice1.UpdateReservation()
                elif choice == 3:
                    reservationservice1.CancelReservation()
                elif choice == 4:
                    reservationservice1.GetReservationById()
                elif choice == 5:
                    reservationservice1.GetReservationsByCustomerId()
                elif choice == 6:
                    reservationservice1.select()
                else:
                    break

        elif choice == 4:
            while True:
                print("1.Add Admin\t2.Update Admin\t3.Delete Admin\n4.Get Admin Details by "
                      "ID\t5.Get Admin Details bu username\t6.View Admins \n7.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    adminservice1.RegisterAdmin()
                elif choice == 2:
                    adminservice1.UpdateAdmin()
                elif choice == 3:
                    adminservice1.DeleteAdmin()
                elif choice == 4:
                    adminservice1.GetAdminById()
                elif choice == 5:
                    adminservice1.GetAdminByUsername()
                elif choice == 6:
                    adminservice1.select()
                else:
                    break

        elif choice == 5:
            while True:
                print("1.Customer Login\n2.Admin Login\n3.Exit")
                choice = int(input("enter ur number"))
                if choice ==1:
                    customerservice1.authenticate_customer()
                elif choice == 2:
                    adminservice1.authenticate_password()
                else:
                    break
        else:
            loop = False
except Exception as e:
    print(e)
