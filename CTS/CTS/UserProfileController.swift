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
    var user = String()
    override func viewDidLoad()
    {
        super.viewDidLoad()
        
        
        let defaults = NSUserDefaults.standardUserDefaults()

        if let usr = defaults.stringForKey("userName")
        {
            lblUserName.text = usr + "\'s"
            self.user = usr
            request(.GET, "http://4350.intpointer.com/api/getProfile/", parameters: ["user": self.user])
                .responseJSON { (_, _, reJson, _) in
                    var profile = JSON(reJson!)
                    self.lblHeight.text = profile["profile"][0]["height"].stringValue
                    self.lblGender.text = profile["profile"][0]["gender"].stringValue
                    self.lblWeight.text = profile["profile"][0]["weight"].stringValue
            }
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