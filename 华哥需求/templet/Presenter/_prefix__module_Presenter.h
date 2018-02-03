//
//  <prefix><module>Presenter.h
//  test2
//
//  Created by <author> on <time>
//  Copyright © <year>年 <author>. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "<prefix><module>ControllerDelegate.h"

@interface <prefix><module>Presenter : NSObject
-(instancetype)initWithViewDelegate:(id<<prefix><module>ViewControllerDelegate>)delegate;
#pragma mark--业务方法
 @end
