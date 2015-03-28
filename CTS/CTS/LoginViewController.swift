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
            if(loginCheck()){
                self.performSegueWithIdentifier("login", sender: self)
            }else{
                var alert = UIAlertController(title: "Alert", message: "Login failed.", preferredStyle: UIAlertControllerStyle.Alert)
                alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
                self.presentViewController(alert, animated: true, completion: nil)
            }
        }
    }
    
    
    
    @IBAction func registerClicked(sender: UIButton) {
        hideInputPanel()
        if (inputCheck()){
            var alert = UIAlertController(title: "Confirm", message: "Please input you password again.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style:UIAlertActionStyle.Default) {
                (action: UIAlertAction!) -> Void in
                var passwordC = alert.textFields?.first as UITextField
                var password = self.passwordL.text
                if (passwordC.text == password){
                    if (self.registerCheck()){
                        var alert = UIAlertController(title: "Register Done", message: "", preferredStyle: UIAlertControllerStyle.Alert)
                        alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
                        self.presentViewController(alert, animated: true, completion: nil)
                    }else{
                        self.showAlert("Register faild.")
                    }
                }else{
                    self.showAlert("Password not match.")
                }
                
            })
            
            alert.addTextFieldWithConfigurationHandler {
                (textField: UITextField!) -> Void in
                textField.placeholder = "confirm password"
                textField.secureTextEntry = true
            }
            self.presentViewController(alert, animated: true, completion: nil)
        }
    }
    
    func hideInputPanel(){
        self.accountL.resignFirstResponder()
        self.passwordL.resignFirstResponder()
    }
    
    func loginCheck()->Bool{
        //----------------------------------------------------------------------
        return true
    }
    
    func registerCheck()->Bool{
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
        }else if(account.utf16Count>30){
            showAlert("Username should be no more than 30 chars.")
            return false
        }else if(account.utf16Count<10){
            showAlert("Username should be no less than 10 chars.")
            return false
        }else if(password.utf16Count>15){
            showAlert("Password should be no more than 15 chars.")
            return false
        }else if(password.utf16Count<6){
            showAlert("Password should be no less than 6 chars.")
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
        var alert = UIAlertController(title: "Alert", message: msg, preferredStyle: UIAlertControllerStyle.Alert)
        alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
        self.presentViewController(alert, animated: true, completion: nil)
    }
    
    
    
    override func touchesBegan(touches: NSSet, withEvent event: UIEvent) {
        self.view.endEditing(true)
    }
    
}
