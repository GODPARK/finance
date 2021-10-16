package com.finance.data.config;

import com.finance.data.component.TokenComponent;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebMvcConfig implements WebMvcConfigurer {

    @Override
    public void addInterceptors (InterceptorRegistry interceptorRegistry) {
        interceptorRegistry.addInterceptor(new TokenComponent())
                .addPathPatterns("/api/**");
    }
}
