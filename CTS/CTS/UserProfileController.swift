//
//  UserProfileController.swift
//  CTS
//
//  Created by Mooska Mayel on 2015-03-28.
//  Copyright (c) 2015 Comp4350Team7. All rights reserved.
//

import UIKit


class UserProfileController : UIViewController
{

    @IBOutlet weak var lblUserName: UILabel!
    @IBOutlet weak var lblHeight: UILabel!
    @IBOutlet weak var lblWeight: UILabel!
    @IBOutlet weak var lblSuggest: UILabel!
    @IBOutlet weak var lblBMI: UILabel!
    @IBOutlet weak var lblGender: UILabel!
   
    @IBOutlet weak var lblTitle: UILabel!
    var labelTxt = String()
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        let defaults = NSUserDefaults.standardUserDefaults()
        if let weight = defaults.stringForKey("weight")
        {
            lblWeight.text = weight
        }
        if let usr = defaults.stringForKey("userName")
        {
            lblUserName.text = usr + "\'s"
            
        }
        if let bmi = defaults.stringForKey("BMI")
        {
            lblBMI.text = bmi
            
        }
        if let height = defaults.stringForKey("height")
        {
            lblHeight.text = height
            
        }
        
    }
    
    @IBAction func logOut(sender: UIButton)
    {
        navigationController?.popToRootViewControllerAnimated(true)
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

}