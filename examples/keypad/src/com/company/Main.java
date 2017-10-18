package com.company;

import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner scan = new Scanner (System.in);
        System.out.println("Please input 4-digits password:");
        int input = scan.nextInt();
        scan.close();

        int [] password = new int [] {9876, 6543, 3210, 1234}; // Password database

        boolean access = checkpassword(password, input); // Password checking processing
        if (access == true) {
            System.out.println("Access Authorized.");
        } else {
            System.out.println("Access Denied, try again.");
        }
        return;
    }

    // Checking logic
    public static boolean checkpassword(int [] password, int input) {
        boolean access = false;
        for (int i = 0; i < password.length; i++) {
            if(input == password[i]) {
                access = true;
            }
        }
        return access;
    }
}

