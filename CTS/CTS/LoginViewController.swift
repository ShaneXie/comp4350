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
    }
    
    func hideInputPanel(){
        self.accountL.resignFirstResponder()
        self.passwordL.resignFirstResponder()
    }
    
    func loginCheck()->Bool{
        return true
    }
    
    func inputCheck()->Bool{
        var account = self.accountL.text
        var password = self.passwordL.text
        if(account.utf16Count==0 || password.utf16Count==0){
            var alert = UIAlertController(title: "Alert", message: "Neither username nor password should be empty.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
            return false
        }else if(account.utf16Count>30){
            var alert = UIAlertController(title: "Alert", message: "Username should be no more than 30 chars.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
            return false
        }else if(account.utf16Count<10){
            var alert = UIAlertController(title: "Alert", message: "Username should be no less than 10 chars.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
            return false
        }else if(password.utf16Count>15){
            var alert = UIAlertController(title: "Alert", message: "Password should be no more than 15 chars.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
            return false
        }else if(password.utf16Count<6){
            var alert = UIAlertController(title: "Alert", message: "Password should be no less than 6 chars.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
            return false
        }
        return true
    }
    
    
    
    override func touchesBegan(touches: NSSet, withEvent event: UIEvent) {
        self.view.endEditing(true)
    }
    
}
