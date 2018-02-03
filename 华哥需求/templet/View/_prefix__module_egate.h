//
//  <prefix><module>ViewControllerDelegate.h
//  test2
//
//  Created by <author> on <time>
//  Copyright © <year>年 <author>. All rights reserved.
//

#ifndef <prefix><module>ViewControllerDelegate_h
#define <prefix><module>ViewControllerDelegate_h

@protocol <prefix><module>ViewControllerDelegate <NSObject>
@optional
- (void)refresh:(NSString *)key data:(id)data;
@end
#endif
