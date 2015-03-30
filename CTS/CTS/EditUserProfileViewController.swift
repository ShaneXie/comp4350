//
//  EditUserProfileViewController.swift
//  CTS
//
//  Created by Mooska Mayel on 2015-03-29.
//  Copyright (c) 2015 Comp4350Team7. All rights reserved.
//

import UIKit

class EditUserProfileViewController: UIViewController
{
    
    @IBOutlet weak var txtWeight: UITextField!
    @IBOutlet weak var txtHeigth: UITextField!
    @IBOutlet weak var txtGender: UITextField!
    @IBOutlet weak var txtBMI: UITextField!
    
    @IBOutlet weak var lblTitle: UILabel!
    override func viewDidLoad()
    {
        super.viewDidLoad()
        lblTitle.textAlignment = NSTextAlignment.Center
        
    }
    func myAlertMsg(usrMsg: String){
        let alert = UIAlertView()
        alert.title = "Alert"
        alert.message = usrMsg
        alert.addButtonWithTitle("Ok")
        alert.show()
    }
    @IBAction func savePressed(sender: AnyObject)
    {
        if(txtBMI.text.isEmpty || txtGender.text.isEmpty || txtWeight.text.isEmpty || txtHeigth.text.isEmpty)
        {
            myAlertMsg("All Fields Are Required!")
            return
        }
        else
        {
            let saveVar  = NSUserDefaults.standardUserDefaults()
            saveVar.setObject(txtWeight.text, forKey: "weight")
            saveVar.setObject(txtHeigth.text, forKey: "heigth")

           // performSegueWithIdentifier("backToProfile", sender: nil)
        }
    }
}
