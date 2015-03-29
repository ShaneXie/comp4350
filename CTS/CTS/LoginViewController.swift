//
//  LoginViewController.swift
//  CTS
//
//  Created by Chuck on 2015-03-26.
//  Copyright (c) 2015 Comp4350Team7. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    /*
    // MARK: - Navigation
    
    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
    // Get the new view controller using segue.destinationViewController.
    // Pass the selected object to the new view controller.
    }
    */
    
    
    @IBOutlet weak var accountL: UITextField!
    @IBOutlet weak var passwordL: UITextField!
    @IBOutlet weak var loginB: UIButton!
    @IBOutlet weak var registerB: UIButton!
    
    
    @IBAction func loginClicked(sender: UIButton) {
        hideInputPanel()
        if (inputCheck()){
            loginCheck()
        }
    }
    
    
    
    @IBAction func registerClicked(sender: UIButton) {
        hideInputPanel()
        if (inputCheck()){
            if (self.registerCheck()){
                let alert = UIAlertView()
                alert.title = "Register done"
                alert.message = ""
                alert.addButtonWithTitle("Ok")
                alert.show()
            }else{
                self.showAlert("Register faild.")
            }
        }
    }
    
    
   
        
    func hideInputPanel(){
        self.accountL.resignFirstResponder()
        self.passwordL.resignFirstResponder()
    }
    
    
    func loginCheck(){
        var account = self.accountL.text
        var password = self.passwordL.text
        var ret = false
        let para = ["loginEmailName":account, "loginPwdName":password]
        //----------------------------------------------------------------------
        request(.POST, "http://127.0.0.1:8000/ajax/login/", parameters: para)
            .responseString { (_, _, string, _) in
                if string == "success"{
                    self.performSegueWithIdentifier("login", sender: self)
                }else{
                    self.showAlert(string!)
                }
            }
    }
    
    func registerCheck()->Bool{
        var account = self.accountL.text
        var password = self.passwordL.text
        //----------------------------------------------------------------------
        return true
    }
    
    
    func inputCheck()->Bool{
        let illegal = "; : ' \" \\ / ~ ` ! # $ % ^ & * ? |".componentsSeparatedByString(" ")
        var account = self.accountL.text
        var password = self.passwordL.text
        if(account.utf16Count==0 || password.utf16Count==0){
            showAlert("Neither username nor password should be empty.")
            return false
        }else {
            for c in illegal{
                if (account.rangeOfString(c)?.startIndex != nil){
                    showAlert("Illegal chars found in username: ; : ' \" \\ / ~ ` ! # $ % ^ & * ? |")
                    return false
                }
                if (password.rangeOfString(c)?.startIndex != nil){
                    showAlert("Illegal chars found in password: ; : ' \" \\ / ~ ` ! # $ % ^ & * ? |")
                    return false
                }

            }
            
        }
        return true
    }
    
    
    func showAlert(msg: String){
        let alert = UIAlertView()
        alert.title = "Alert"
        alert.message = msg
        alert.addButtonWithTitle("Ok")
        alert.show()
    }
    
    
    
    override func touchesBegan(touches: NSSet, withEvent event: UIEvent) {
        self.view.endEditing(true)
    }
    
}
